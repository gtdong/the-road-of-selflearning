<<<<<<< HEAD
# 练习题

 1.简述编译型与解释型语言的区别，且分别列出你知道的哪些语言属于编译型，哪些属于解释型?
   编译型语言的代码在运行时需要事先编译成计算机可识别的机器码，然后再运行，效率较高
   解释型语言不需要事先编译，代码是一边解释一边运行的，效率较低低

 2.执行 Python 脚本的两种方式是什么?
   第一种: python xxx.py
   第二种: ./xxx.py (需要赋予xxx.py执行权限)

 3.Pyhton 单行注释和多行注释分别用什么?
   单行注视用 #单行注释
   多行注释用 '''多行注释'''

 4.布尔值分别有什么?
   True 和 False

 5.声明变量注意事项有那些?
   (1)可以由数字、字母、下划线组合
   (2)不能以数字开头
   (3)不能与系统关键字保留字重名
   (4)见名知意，建议使用_连接语法（驼峰 owenName OwenName | _连接  owen_name），一般_开头或结尾都有特殊含义

 6.如何查看变量在内存中的地址?
   id("变量名")
 7.现有如下两个变量,请简述 n1 和 n2 是什么关系?
       n1 = 123456
       n2 = n1
   n1和n2的变量值相同，都是123456，并且n1和n2指向同一个内存地址

 8.写代码
 (1)实现用户输入用户名和密码,当用户名为 seven 且 密码为 123 时,显示登陆成功,否则登陆失败!
 (2)实现用户输入用户名和密码,当用户名为 seven 且 密码为 123 时,显示登陆成功,否则登陆失败,失败时允许重复输入三次
 (3)实现用户输入用户名和密码,当用户名为 seven 或 alex 且 密码为 123 时,显示登陆成功,否则登陆失败,失败时允许重复输入三次
 (4)使用while循环实现输出2-3+4-5+6...+100 的和
 (5)使用 while 循环实现输出 1,2,3,4,5, 7,8,9, 11,12 使用 while 循环实现输出 1-100 内的所有奇数
 (6)使用 while 循环实现输出 1-100 内的所有偶数


 (1)
 Username = input("请输入你的用户名:")
 Password = input("请输入你的密码:")
 if Username == "seven" and Password == "123":
     print("登录成功")
 else:
     print("登录失败")
 (2)
 err_times = 0
 while err_times < 3:
     Username = input("请输入你的用户名:")
     Password = input("请输入你的密码:")
     if Username == "seven" and Password == "123":
         print("登录成功")
         break
     else:
         print("登录失败")
         err_times += 1
         continue
 (3)
 i = 0
 while i < 3:
     Username = input("请输入你的用户名:")
     Password = input("请输入你的密码:")
     if Username == "seven" or "alex" and Password == "123":
         print("登录成功")
         break
     else:
         print("登录失败")
         i = i +1
         continue

 (4)
 num = 2
 sum = 0

 while num <= 100:
     if num % 2 == 0:
         sum = sum + num
     else:
         sum = sum - num
     num += 1
 print(sum)

 (5)
 n = 1
 while n <= 12:
     if n != 6 and n != 10:
         print(n)
     n += 1
 while n <= 100:
     if n % 2 == 1:
         print(n)
     n += 1
 (6)
 n=2
 while n <= 100:
     if n % 2 == 0:
         print(n)
       n += 1

 9.编写登陆接口'''
 (1).基础需求
   . 让用户输入用户名密码
   . 认证成功后显示欢迎信息
   . 输错三次后退出程序


 username = 'owen'
 password = '123123'
 count = 1
 while count <=3 :
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

 (2).升级需求
 . 可以支持多个用户登录 (提示，通过列表存多个账户信息)
 . 用户3次认证失败后，退出程序，再次启动程序尝试登录时，还是锁定状态（提示:需把用户锁定的状态存到文件里
=======
# 练习题
#
# 1.简述编译型与解释型语言的区别，且分别列出你知道的哪些语言属于编译型，哪些属于解释型?
#   编译型语言的代码在运行时需要事先编译成计算机可识别的机器码，然后再运行，效率较高
#   解释型语言不需要事先编译，代码是一边解释一边运行的，效率较低低
#
# 2.执行 Python 脚本的两种方式是什么?
#   第一种: python xxx.py
#   第二种: ./xxx.py (需要赋予xxx.py执行权限)
#
# 3.Pyhton 单行注释和多行注释分别用什么?
#   单行注视用 #单行注释
#   多行注释用 '''多行注释'''
#
# 4.布尔值分别有什么?
#   True 和 False
#
# 5.声明变量注意事项有那些?
#   (1)可以由数字、字母、下划线组合
#   (2)不能以数字开头
#   (3)不能与系统关键字保留字重名
#   (4)见名知意，建议使用_连接语法（驼峰 owenName OwenName | _连接  owen_name），一般_开头或结尾都有特殊含义
#
# 6.如何查看变量在内存中的地址?
#   id("变量名")
# 7.现有如下两个变量,请简述 n1 和 n2 是什么关系?
#       n1 = 123456
#       n2 = n1
#   n1和n2的变量值相同，都是123456，并且n1和n2指向同一个内存地址
#
# 8.写代码
# (1)实现用户输入用户名和密码,当用户名为 seven 且 密码为 123 时,显示登陆成功,否则登陆失败!
# (2)实现用户输入用户名和密码,当用户名为 seven 且 密码为 123 时,显示登陆成功,否则登陆失败,失败时允许重复输入三次
# (3)实现用户输入用户名和密码,当用户名为 seven 或 alex 且 密码为 123 时,显示登陆成功,否则登陆失败,失败时允许重复输入三次
# (4)使用while循环实现输出2-3+4-5+6...+100 的和
# (5)使用 while 循环实现输出 1,2,3,4,5, 7,8,9, 11,12 使用 while 循环实现输出 1-100 内的所有奇数
# (6)使用 while 循环实现输出 1-100 内的所有偶数
#
#
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
# (4)
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
#
# (5)
# n = 1
# while n <= 12:
#     if n != 6 and n != 10:
#         print(n)
#     n += 1
# while n <= 100:
#     if n % 2 == 1:
#         print(n)
#     n += 1
# (6)
# n=2
# while n <= 100:
#     if n % 2 == 0:
#         print(n)
#       n += 1
#
# 9.编写登陆接口'''
# (1).基础需求
#   . 让用户输入用户名密码
#   . 认证成功后显示欢迎信息
#   . 输错三次后退出程序
#
#
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

# (2).升级需求
# . 可以支持多个用户登录 (提示，通过列表存多个账户信息)
# . 用户3次认证失败后，退出程序，再次启动程序尝试登录时，还是锁定状态（提示:需把用户锁定的状态存到文件里
>>>>>>> 4d1a71eb2dbb4a11a14c9db25599d4c1bba3c678
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

