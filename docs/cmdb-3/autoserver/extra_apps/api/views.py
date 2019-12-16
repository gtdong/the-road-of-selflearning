from django.shortcuts import HttpResponse
import json
from repository import models

# Create your views here.
def getInfo(request):
    result = request.body
    # print(type(result))
    print(result.decode())
    return HttpResponse('ok')


server_key = "skfngksdgnfkjdsgnfdskjgs"
def asset(request):
    if request.method == 'GET':
        client_key = request.META.get('HTTP_KEY')
        # if server_key != client_key:
        #     return HttpResponse('非法请求')

        import hashlib, time

        client_md5_key,client_time = client_key.split('|')

        server_time = time.time()
        client_time = float(client_time)
        if server_time - client_time > 10:
            return HttpResponse('第一关，时间失效')

        tmp = "%s|%s" % (server_key, client_time)

        m = hashlib.md5()
        m.update(bytes(tmp, encoding='utf8'))
        server_md5_key = m.hexdigest()

        if client_md5_key != server_md5_key:
            return HttpResponse('第二关，加密出错')


        ##### 第三关，连接redis,设置key的过期时间 20s

        return HttpResponse('ok')
    elif request.method == 'POST':
        # print(request.body)
        res = request.body
        new_server_info = json.loads(res)

        # print(new_server_info)

        hostname = new_server_info['basic']['data']['hostname']
        old_server_obj = models.Server.objects.filter(hostname=hostname).first()
        # print(old_server_obj)

        if not old_server_obj:
            return HttpResponse('服务器资产不存在')

        ### 处理分析数据 以分析disk数据为例
        status = new_server_info['disk']['status']
        if status != 10000:
            models.ErrorLog.objects.create(asset_obj=old_server_obj, title='(%s)采集出错' % hostname, content=new_server_info['disk']['data'])

        old_disk_info = models.Disk.objects.filter(server_obj=old_server_obj)
        new_disk_info = new_server_info['disk']['data']
        # print(new_disk_info)

        new_slot_list = list(new_disk_info.keys())
        old_slot_list = []
        for v in old_disk_info:
            old_slot_list.append(v.slot)

        #1.增加的slot
        add_slot_list = set(new_slot_list).difference(set(old_slot_list))
        # print(add_slot_list)

        if add_slot_list:
            recoder_list = []
            for v in add_slot_list:
                disk_res = new_disk_info[v]
                tmp = "增加磁盘槽位{slot},类型{pd_type},容量{capacity},型号{model}".format(**disk_res)
                disk_res['server_obj'] = old_server_obj
                models.Disk.objects.create(**disk_res)
                recoder_list.append(tmp)

            recoder_str = ";".join(recoder_list)
            models.AssetRecord.objects.create(asset_obj=old_server_obj, content=recoder_str)

    #2.删除的slot
        del_slot_list = set(old_slot_list).difference(set(new_slot_list))
        # print(del_slot_list)

        if del_slot_list:
            models.Disk.objects.filter(slot__in=del_slot_list, server_obj=old_server_obj).delete()
            del_str = "删除的槽位是%s" % (";".join(del_slot_list))
            models.AssetRecord.objects.create(asset_obj=old_server_obj, content=del_str)

    #3.更新的slot
        up_slot_list = set(old_slot_list).intersection(set(new_slot_list))
        # print(up_slot_list)

        if up_slot_list:
            recoder_list = []
            for slot in up_slot_list:
                old_disk_row = models.Disk.objects.filter(slot=slot, server_obj=old_server_obj).first()
                new_disk_row = new_disk_info[slot]
                for k, new_v in new_disk_row.items():
                    '''
                    k: slot, pd_type, model
                    '''
                    old_v = getattr(old_disk_row,k)
                    if old_v != new_v:
                        tmp = "槽位：%s,%s由%s更改为%s" % (slot,k,old_v,new_v)
                        recoder_list.append(tmp)
                        setattr(old_disk_row,k,new_v)
                    old_disk_row.save()

            if recoder_list:
                models.AssetRecord.objects.create(asset_obj=old_server_obj, content=";".join(recoder_list))




        return HttpResponse('ok')


