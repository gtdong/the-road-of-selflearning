'''
写用户功能层
'''
from interface import user_interface, bank_interface, shop_interface
from lib import common

user_info = {
    'name': None
}


# 注册
def register():
    while True:
        # 用户功能层
        user = input('请输入用户名:').strip()
        pwd = input('请输入密码:').strip()
        re_pwd = input('请确认密码:').strip()
        if pwd == re_pwd:

            # 调用注册接口
            # msg == '%s注册成功' % user
            # (True, %s注册成功)  or  (False,用户已存在)
            flag, msg = user_interface.register_interface(user, pwd)

            if flag:
                print(msg)
                break
            else:
                print(msg)


# 登录
def login():
    while True:
        user = input('请输入用户名:').strip()
        pwd = input('请输入密码:').strip()
        # True 登录成功、False 用户不存   密码错误
        flag, msg = user_interface.login_interface(user, pwd)
        if flag:
            print(msg)
            # 登录成功做一次记录
            user_info['name'] = user
            break
        else:
            print(msg)


# 查看余额
@common.login_auth
def check_balance():
    balance = user_interface.check_bal_interface(user_info['name'])
    print('尊敬的用户[%s]，您的余额为[%s]' % (user_info['name'], balance))


# 提现
@common.login_auth
def withdraw():
    while True:
        money = input('请输入提现金额:').strip()
        if money.isdigit():
            money = int(money)
            # 调用提现接口
            flag, msg = bank_interface.withdraw_interface(user_info['name'], money)
            if flag:
                print(msg)
                break
            else:
                print(msg)


# 转账
@common.login_auth
def transfer():
    while True:
        to_user = input('请输入转账目标用户:').strip()
        money = input('请输入转账金额:').strip()

        if money.isdigit():
            money = int(money)

            flag, msg = bank_interface.transfer_interface(user_info['name'], to_user, money)
            if flag:
                print(msg)
                break
            else:
                print(msg)


# 还款
@common.login_auth
def repay():
    while True:
        money = input('请输入还款金额:').strip()
        if money.isdigit():
            money = int(money)

            msg = bank_interface.repay_interface(user_info['name'], money)
            print(msg)
            break
        else:
            print('请输入数字')


# 查看流水
@common.login_auth
def check_flow():
    # 调用流水接口
    flow_list = bank_interface.flow_interface(user_info['name'])
    for flow in flow_list:
        print(flow)


# 购物车功能
@common.login_auth
def shopping_car():
    # 获取用户当前余额
    user_balance = user_interface.check_bal_interface(user_info['name'])

    # 设置一个空的购物车
    # 以商品名称作为key，以商品数量作为value
    shopping_car_s = {}

    # 商品的总价
    cost = 0

    while True:
        goods_list = [
            ['凤爪', 50],
            ['肠粉', 20],
            ['macbook pro', 10000],
            ['肥仔快乐水', 5]
        ]

        # for good_list in goods_list:
        # 0  ['凤爪', 50]
        for index, goods in enumerate(goods_list):
            print(index, goods)

        choose_num = input('请输入商品编号:').strip()

        if not choose_num.isdigit():
            print('请输入数字')
            continue
        choose_num = int(choose_num)

        if choose_num >= 0 and choose_num < len(goods_list):

            # ['凤爪', 50]
            # 获取商品的名称、单价
            good, price = goods_list[choose_num]

            if user_balance >= price:

                # 判断购物车内商品是否存在，存在+1，不存在设置为1
                if good in shopping_car_s:
                    shopping_car_s[good] += 1
                else:
                    shopping_car_s[good] = 1

                # 计算总价
                cost += price

                sure = input('确认购买？ 请输入 y/n:').strip()

                if sure == 'y':
                    # 调用结账接口
                    flag, msg = shop_interface.pay_interface(user_info['name'], cost)

                    if flag:
                        print(msg)
                        break

                elif sure == 'n':

                    # 调用添加购物车接口
                    msg = shop_interface.save_shop_car_interface(user_info['name'], shopping_car_s)
                    print(msg)
                    break

            else:
                print('用户余额不足!')

        else:
            print('请输入商品编号！')


# 查看购物车
@common.login_auth
def check_shopping_car():
    shop_car_s = shop_interface.check_shop_car_interface(user_info['name'])
    print(shop_car_s)


# 注销
@common.login_auth
def logout():
    user_info['name'] = None


# 选择功能的字典
func_dic = {
    '1': register,
    '2': login,
    '3': check_balance,
    '4': withdraw,
    '5': transfer,
    '6': repay,
    '7': check_flow,
    '8': shopping_car,
    '9': check_shopping_car,
    '10': logout,
}


def run():
    while True:
        print('''
            1.注册
            2.登录
            3.查看余额
            4.提现
            5.转账
            6.还款
            7.查看流水
            8.购物车功能
            9.查看购物车
            10.注销
            q.退出
        ''')

        choose = input('请输入功能编号:').strip()

        if choose == 'q':
            break

        if choose not in func_dic:
            print('请选择功能的编号!')
            continue

        # 调用用户选择的功能
        func_dic[choose]()
