# '''练习题'''
#
# 1.区别:编译型语言的代码在运行时需要事先编译成计算机可识别的机器码，然后再运行，效率较高
#        解释型语言不需要事先编译，代码是一边解释一边运行的，效率较低低
#
# 2.第一种: python xxx.py
#   第二种: ./xxx.py (需要赋予xxx.py执行权限)
#
# 3.单行注视用 #单行注释
#   多行注释用 '''多行注释'''
#
# 4.True 和 False
#
# 5.(1)变量名可以是数字、字母、下划线的组合
#   (2)变量名不能以数字开头
#   (3)变量名最好不要使用python中已有的
#
# 6.id("变量名")
#
# 7.
# (1)
# Username = input("请输入你的用户名:")
# Password = input("请输入你的密码:")
# if Username == "seven" and Password == "123":
#     print("登录成功")
# else:
#     print("登录失败")
# (2)
# err_times = 0
# while err_times < 3:
#     Username = input("请输入你的用户名:")
#     Password = input("请输入你的密码:")
#     if Username == "seven" and Password == "123":
#         print("登录成功")
#         break
#     else:
#         print("登录失败")
#         err_times += 1
#         continue
# (3)
# i = 0
# while i < 3:
#     Username = input("请输入你的用户名:")
#     Password = input("请输入你的密码:")
#     if Username == "seven" or "alex" and Password == "123":
#         print("登录成功")
#         break
#     else:
#         print("登录失败")
#         i = i +1
#         continue
#
# 8.
# (1)
# num = 2
# sum = 0
#
# while num <= 100:
#     if num % 2 == 0:
#         sum = sum + num
#     else:
#         sum = sum - num
#     num += 1
# print(sum)
# # (2)
# n = 1
# while n <= 12:
#     if n != 6 and n != 10:
#         print(n)
#     n += 1
# while n <= 100:
#     if n % 2 == 1:
#         print(n)
#     n += 1
# (3)
# n=2
# while n <= 100:
#     if n % 2 == 0:
#         print(n)
#       n += 1
#
# 9.n1和n2的变量值相同，都是123456，并且n1和n2指向同一个内存地址
#
#
# '''作业'''
# #1.基础需求
# username = 'owen'
# password = '123123'
# count = 1
# while count <=3 :
#     username_input = input("请输入您的用户名:")
#     if username_input != username:
#         print("此用户不存在，请重新输入")
#         count += 1
#         continue
#     password_input = input("请输入你的密码:")
#     if username_input == username and password_input == password:
#         print("登录成功！")
#         break
#     else:
#         print("密码错误,请重新输入:")
#         count += 1
#         continue
# else:
#     print("输入次数过多，退出！")

# 2.升级需求
users = {
    'owen1': {'pwd': '123', 'err_times': 0},
    'owen2': {'pwd': '456', 'err_times': 0},
    'owen3': {'pwd': '789', 'err_times': 0}
}  # 用户名密码


def main():
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

if __name__ == '__main__':
    main()

