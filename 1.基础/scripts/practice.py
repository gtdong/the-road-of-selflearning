# 9.编写登陆接口'''
# (1).基础需求
#   . 让用户输入用户名密码
#   . 认证成功后显示欢迎信息
#   . 输错三次后退出程序
def user_login():
    username = 'owen'
    password = '123123'
    count = 1
    while count <= 3:
        username_input = input("请输入您的用户名:")
        if username_input != username:
            print("此用户不存在，请重新输入")
            count += 1
            continue
        password_input = input("请输入你的密码:")
        if username_input == username and password_input == password:
            print("登录成功！")
            break
        else:
            print("密码错误,请重新输入:")
            count += 1
            continue
    else:
        print("输入次数过多，退出！")

user_login()
#
# (2).升级需求
# . 可以支持多个用户登录 (提示，通过列表存多个账户信息)
# . 用户3次认证失败后，退出程序，再次启动程序尝试登录时，还是锁定状态（提示:需把用户锁定的状态存到文件里
users = {
    'owen1': {'pwd': '123', 'err_times': 0},
    'owen2': {'pwd': '456', 'err_times': 0},
    'owen3': {'pwd': '789', 'err_times': 0}
}  # 用户名密码


def user_login2():
    while True:
        username_input = input("请输入您的用户名:")  # 1.输入用户名，密码
        password_input = input("请输入你的密码:")

        if username_input in users:  # 2.判断用户是否存在
            with open('lock_users', 'r') as f:
                lock_username = f.read().rstrip(",").split(",")
            if username_input in lock_username:
                print("该用户已被锁定！")
                break
            elif password_input == users[username_input]['pwd']:  # 3.判断密码是否正确
                print("登录成功！")
                break
            else:
                print("密码错误!")
                users[username_input]['err_times'] += 1
                if users[username_input]['err_times'] == 3:
                    print("输入次数过多,账户已锁定！")  # 4.锁定输入次数过多的用户,并且写入到文件里
                    with open('lock_users', 'a') as f:
                        f.write("%s," % username_input)
                    break
        else:
            print('该用户不存在')
# user_login2()

