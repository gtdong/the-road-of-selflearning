# 1.统计元组中所有数据属于字符串的个数，提示：isinstance()
# 数据：t1 = (1, 2, '3', '4', 5, '6')
# 结果：3

def str_count():
    t1 = (1, 2, '3', '4', 5, '6')
    str_count = 0
    for string in t1:
        if isinstance(string, str):
            str_count += 1
    print(str_count)


str_count()


# 2.将以下数据存储为字典类型
# 数据：info = "name:Owen|age:18|gender:男"
# 结果：{'name': 'Owen', 'age': 18, 'gender': '男'}
# 注：年龄存储为数字类型
#
def str_to_dic():
    info = "name:Owen|age:18|gender:男"
    list1 = info.split("|")
    dict = {}
    for l1 in list1:
        l2 = l1.split(":")
        if l2[0] == 'age':
            dict[l2[0]] = int(l2[1])
        else:
            dict[l2[0]] = l2[1]
    print(dict)


str_to_dic()


# 3.完成数据的去重
# 数据：t3 = (1, 2, 1, 2, 3, 5, 9)
# 结果：t3 = (1, 2, 3, 5, 9)
# 注：从不考虑顺序、考虑顺序两方面完成
#
#
def data_duplicate():
    t3 = (1, 2, 1, 2, 3, 5, 9)
    print(tuple(set(t3)))


# data_duplicate()
def data_duplicate2():
    t3 = (1, 2, 1, 2, 3, 5, 9)
    list1 = []
    for i in t3:
        if i not in list1:
            list1.append(i)

    t3 = tuple(list1)
    print(t3)


data_duplicate2()


# 4.计算元组中所有可以转换为数字的数据的总和
# 数据：t4 = (10, 'abc', '100', '3')
# 运算结果：113
def tuple_str_count():
    t4 = (10, 'abc', '100', '3')
    sum = 0
    for t in t4:
        if isinstance(t, int):
            sum = sum + t
        else:
            if t.isdigit():
                sum = sum + int(t)
    print(sum)


tuple_str_count()


# 5.将数据转换类型存储
# 原数据：dic = {'name': 'Owen', 'age': 18, 'gender': '男'}
# 处理后：info = [('name', 'Owen'), ('age', 18), ('gender', '男')]
#
#
def dic_to_list():
    dic = {'name': 'Owen', 'age': 18, 'gender': '男'}
    info = []
    for item in dic.items():
        info.append(item)
    print(info)


dic_to_list()


# 拓展：选做
# 1.计算元组中所有可以转换为数字的数据的总和
# 数据：t4 = (10, 'abc', '100', '3', '壹', '肆', [1000], (10000,))
# 运算结果：11118
# 提示：
#   -- 利用字符串isnumeric()判断汉字
# 	-- 利用字典{'壹': 1 ...}将汉字转换为数字
#	-- 利用isinstance()将list和tuple中数据取出来
#	-- 先将所有转化为数字的数据存放在一个单列集合中，在做运算
def strCount():
    t5 = (10, 'abc', '100', '3', '壹', '肆', [1000], (10000,))
    sum = 0
    for t in t5:
        if isinstance(t, int):
            sum = sum + t
        elif isinstance(t, str):
            if t.isdigit():
                sum = sum + int(t)
            elif t.isnumeric():
                if t == '壹':
                    sum = sum + 1
                else:
                    sum = sum + 4
        elif isinstance(t, list) or isinstance(t, tuple):
            sum = sum + t[0]

    print(sum)


strCount()

# 2.完成录入电话本
# 需求：
'''
-- 从键盘中录入姓名(不区分大小写)：
	-- 姓名必须是全英文组成，不是则重新录入姓名，如果是q，代表退出
-- 从键盘中再录入电话：
	-- 电话必须为数字且长度必须是11位(不能转换为数字)
-- 如果出现姓名相同，则保留最后一次电话号码
-- 形成的数据是有电话分组的，如：第一次录入Owen，13355667788，则会形成
	-- {
    	'O': {
    		'Owen': '13355667788'
    	}
	}



最终数据，分组名一定大写：
{
    'E': {
		'egon': '17788990000',
		'engo': '16633445566'
    },
    'O': {
    	'Owen': '13355667788'
    }
}
'''


def tel_input():
    dic1 = {}
    while True:
        # dict1 = {}
        name = input('please input your name:')
        if not name.isalpha():
            continue
        if name == 'q':
            break
        tel = input('please input your telephone number:')
        if tel == 'q':
            break
        if len(tel) != 11 or not tel.isdigit():
            continue
        dic1[name] = tel
        print('号码录入成功！')
    data = {}
    for key, value in dic1.items():
        dict2 = {key: value}
        if key[0].upper() in data:
            data[key[0].upper()][key] = value
        else:
            data[key[0].upper()] = dict2
    print(data)


# 3.三级菜单
#
# 打印省、市、县三级菜单
# 可返回上一级
# 可随时退出程序
menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车战': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}
def level3_menu():
    while True:#1.第一层
        for k1 in menu:
            print(k1)
        city = input("请输入您要查询的城市，返回上一级按b,退出按q:")
        if city == 'q':
            exit()
        if city == 'b':
            break
        if city not in menu:
            continue

        while True:#2.第二层
            for k2 in menu[city]:
                print(k2)
            area = input("请输入您要查询的区，返回上一级请按b,退出按q:")
            if area == 'q':
                exit()
            if area == 'b':
                break
            if area not in menu[city]:
                continue

            while True:#3.第二层
                for k3 in menu[city][area]:
                    print(k3)
                region = input("请输入您要查询的地区,返回上一级请按b,退出按q:")
                if region == 'q':
                    exit()
                if region == 'b':
                    break
                if region not in menu[city][area]:
                    continue

                while True:#4.第四层
                    for k4 in menu[city][area][region]:
                        print(k4)
                    last_command = input("返回上一级请按b, 退出按q:")
                    if last_command == 'q':
                        exit()
                    elif last_command == 'b':
                        break
                    else:
                        continue
#level3_menu()

#4.请闭眼写出购物车程序
'''
需求:
用户名和密码存放于文件中，格式为：egon|egon123
启动程序后，先登录，登录成功则让用户输入工资,然后打印商品列表，失败则重新登录，超过三次则退出程序
允许用户根据商品编号购买商品
用户选择商品后，检测余额是否够，够就直接扣款
'''
def shopping_cart():
    import os
    count = 1
    while count <=3:
        user_input = input('请输入用户名:')
        pass_input = input('请输入密码:')
        with open('user.txt','r') as f:
            userlist = f.read().split("|")
            username = userlist[0]
            password = userlist[1]
        if user_input == username and pass_input == password:
            print('登录成功！')
            break
        else:
            count += 1
            continue
    else:
        print("输入次数过多,已退出！")
        exit()
    f1 = open('goods.txt')
    f2 = open('prices.txt')
    goodsList = f1.read().splitlines()
    priceList = f2.read().splitlines()
    print('商品的价格如下:')
    print()
    for i in range(4):
        print(i+1,goodsList[i], ' : ', priceList[i])
    f1.close()
    f2.close()
    listbuy = []
    flag = os.path.isfile('balance.txt')
    if flag:
        try:
            f3 = open('balance.txt')
            balancetext = f3.read()
            print()
            print('您当前的余额为: %s' % balancetext)
            balance = int(balancetext)
            f3.close()
        except ValueError:
            pass
    else:
        salary = input('请输入您的薪水:')
        balance = int(salary)
        balanceObject = open('balance.txt', 'w')
        balanceObject.write(str(balance))
        balanceObject.close()

    while True:
        buy = input('请输入您要购买的商品编号:')
        if buy == 'q':
            print('have bought below:', listbuy, ',', 'balance:%s' % balance)
            break
        if int(buy) not in range(1,5):
            print("商品不存在")

        temp = balance - int(priceList[int(buy)-1])
        if temp >= 0:
            balance = balance - int(priceList[int(buy)-1])
            listbuy.append(goodsList[int(buy)-1])
            with open('balance.txt', 'w') as balanceObject:
                balanceObject.write(str(balance))
            balanceObject.close()
            print('add "%s" into your shopping basket' % goodsList[int(buy)-1])
        else:
            print('余额不足')
shopping_cart()