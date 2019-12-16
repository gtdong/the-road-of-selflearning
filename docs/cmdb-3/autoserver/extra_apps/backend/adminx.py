import xadmin
from repository import models
from xadmin import views

class UserProfileAdmin(object):
    list_display = ['id','name','email','phone','mobile']

    search_fields = ['id','name','email','phone']

    list_display_links = ('id',)

    list_editable = ['name','email','phone','mobile']

    list_per_page = 20

    ordering = ('id',)

    readonly_fields = ('email',)

    show_detail_fields = ['asset_name']

xadmin.site.register(models.UserProfile,UserProfileAdmin)


# 全局修改，固定写法
class GlobalSettings(object):
    # 修改title
    site_title = 'CMDB资产管理平台'
    # 修改footer
    site_footer = 'xxx的公司'
    # 收起菜单
    # menu_style = 'accordion'

    # global_search_models = [models.Disk, models.Server]
    # global_models_icon = {
    #     models.Server: "fa fa-linux", models.Disk: "fa fa-cloud", models.UserProfile: "fa fa-user"
    # }


# 将title和footer信息进行注册
xadmin.site.register(views.CommAdminView,GlobalSettings)
# 创建xadmin的最基本管理器配置，并与view绑定
class BaseSetting(object):
    # 开启主题功能
    enable_themes = True
    use_bootswatch = True

# 将基本配置管理与view绑定
xadmin.site.register(views.BaseAdminView,BaseSetting)



class UserProfileAdmin(object):
    list_display = ['id','name' ,'email','phone','mobile']

    search_fields = ['id', 'name', 'email', 'phone']
    list_editable = ['name' ,'email','phone','mobile']
    # list_filter = ['name' ,'email','phone','mobile']
    # list_filter = ['oid','user' ,'odate','oisPay','ototal','oadress']
    show_bookmarks = False



class UserGroupAdmin(object):
    list_display = ['id', 'name', 'users']

    search_fields = ['id', 'name', 'users']
    list_editable = ['name', ]

    # data_charts = {
    #     "user_count": {'title': u"用户分布", "x-field": "name", "y-field": ("id",),},
    #     # "avg_count": {'title': u"Avg Report", "x-field": "date", "y-field": ('avg_count',), "order": ('date',)}
    # }
    show_detail_fields = ['name']


class DiskAdmin(object):
    list_display = ['id','slot' ,'model','capacity','pd_type','server_obj']

    search_fields = ['id', 'slot' ,'model','capacity','pd_type']
    # list_editable = ['name' ,'email','phone','mobile']
    # list_filter = ['name' ,'email','phone','mobile']
    # list_filter = ['oid','user' ,'odate','oisPay','ototal','oadress']


class ServerAdmin(object):
    list_display = ['id', 'device_type_id', 'device_status_id', 'idc', 'business_unit', 'hostname', 'create_at']

    show_detail_fields = ['hostname']
    # search_fields = ['id', 'slot', 'model', 'capacity', 'pd_type']
    # data_charts = {
    #     "user_count": {'title': u"服务器分布", "x-field": "idc", "y-field": ("business_unit",),},
    #     # "avg_count": {'title': u"Avg Report", "x-field": "date", "y-field": ('avg_count',), "order": ('date',)}
    # }
    # list_per_page = 2
    data_charts = {
        "host_service_type_counts": {
            'title': '部门机器使用情况',
            'x-field': "business_unit",
            'y-field': ("business_unit"),
            'option': {
                "series": {"bars": {"align": "center", "barWidth": 0.8, "show": True}},
                "xaxis": {"aggregate": "count", "mode": "categories"}
            },
        },
        "host_idc_counts": {
            'title': '机房统计',
            'x-field': "idc",
            'y-field': ("idc",),
            'option': {
                "series": {"bars": {"align": "center", "barWidth": 0.3, "show": True}},
                "xaxis": {"aggregate": "count", "mode": "categories"}
            }
        }
    }


class IDCAdmin(object):
    list_display = ['id', 'name', 'floor']

    show_detail_fields = ['name']
    # search_fields = ['id', 'slot', 'model', 'capacity', 'pd_type']

class AssetRecordAdmin(object):
    list_display = ['id','content', 'asset_obj']

class ErrorLogAdmin(object):
    list_display = ['id', 'title','content', 'asset_obj']

xadmin.site.register(models.Disk, DiskAdmin)
xadmin.site.register(models.Server, ServerAdmin)
xadmin.site.register(models.IDC, IDCAdmin)
# xadmin.site.register(models.UserProfile, UserProfileAdmin)
xadmin.site.register(models.UserGroup, UserGroupAdmin)
xadmin.site.register(models.AssetRecord, AssetRecordAdmin)
xadmin.site.register(models.ErrorLog, ErrorLogAdmin)
