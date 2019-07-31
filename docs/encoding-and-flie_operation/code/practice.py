# -*- coding: utf-8 -*-

# 1.统计⽂文件数据中字⺟母e出现的次数(不不区分⼤大⼩小写)
# ⽂文件内容:hello friend, can you speak English!
# 结果:4
# with open('1.txt','w') as f:
#   f.write('hello friend, can you speak English!')
with open('1.txt', 'r', encoding='utf-8') as f1:
    data = f1.read()
    count1 = data.count('e')
    count2 = data.count('E')
    count_total = count1 + count2
print(count_total)
# 分析:将⽂文件内容读出，然后统计读出的字符串串中字符e的个数(字符串串count功能)


# 2.统计⽂文件数据中出现的的所有字符与该字符出现的个数(不不区分⼤大⼩小写,标点与空格也算)
# ⽂文件内容:hello friend, can you speak English!
# 结果:
# {
# 'h': 1,
# 'e': 4,
# 'l': 3,
# 'o': 2,
# ' ': 5,
# ...
# }
#
with open('1.txt', 'r', encoding='utf-8') as f2:
    data2 = f2.read()
s_dict = {}
for s in data2:
    if s.isalpha():
        s = s.lower()
    if s not in s_dict:
        s_dict.setdefault(s, 1)
    else:
        s_dict[s] += 1
print(s_dict)

#
# 分析:将⽂文件内容读出，然后统计读出的字符串串中每个字符的个数，形成字段(for遍历读取的字符 串串)
# 3.读取⽂文件内容，分析出所有的账号及对应的密码
# ⽂文件内容:owen:123456|egon:123qwe|liuxx:000000
# 结果:
#
# '''
# {
# 'owen': '123456',
# 'egon': '123qwe',
# 'liuxx': '000000'
# }
with open('2.txt','w') as f:
    f.write('owen:123456|egon:123qwe|liuxx:000000')
with open('2.txt', 'r', encoding='utf-8') as f:
    data3 = f.read()
user_dict = {}
for t in data3.split('|'):
    k, v = t.split(':')
    user_dict[k] = v
print(user_dict)
# # 分析:将⽂文件内容读出，然后按|拆分出 账号:密码 格式的⼦子字符串串，再按:拆分成 账号及密码， 存放到字典中
# # 4.在题3的基础上，账号密码已经被存储在⽂文件中，完成⽤用户登录成功或失败(只做⼀一次性判断) # ⽂文件内容:owen:123456|egon:123qwe|liuxx:000000
# # 需求:输⼊入账号、密码，然后进⾏行行登录判断，账号密码均正确打印登录成功，否则打印登录失败 # 分析:先完成题3，分析出账号密码字典，然后拿输⼊入的账号密码与字典中数据进⾏行行校验
username = input('name:')
password = input('password:')
if password == user_dict[username]:
    print('successful')
else:
    print('failed')

# 5.在题3的基础上，完成⽤用户注册的功能(只做⼀一次性判断)
# ⽂文件内容:owen:123456|egon:123qwe|liuxx:000000
# 需求:输⼊入注册的账号、密码，账号已存在的打印账号已存在，注册失败，反正打印注册成功，并将 新账号密码录⼊入⽂文件
# 结果:如果输⼊入mac、123123 => owen:123456|egon:123qwe|liuxx:000000|mac:123123
# 分析:先完成题3，分析出账号密码字典，然后拿输⼊入的注册账号与字典中数据进⾏行行校验，如果校验 没有新账号
# -- 1.采⽤用 w 模式写⽂文件，可以在读取⽂文件的内容后拼接 |mac:123123 字符串串，将拼接后的总 字符串串⼀一次性写⼊入
# -- 2.采⽤用 a 模式写⽂文件，可以直接追加写⼊入 |mac:123123 字符串串
with open('2.txt', 'r', encoding='utf-8') as f:
    data4 = f.read()
user_dict = {}
for t in data4.split('|'):
    k, v = t.split(':')
    user_dict[k] = v
username = input('name:')
password = input('password:')
if username in data4 and password == user_dict[username]:
    print('account has existed,failed to sign up!')
else:
    data4 = data4 + "|"+username+":"+password
    with open('2.txt', 'w',encoding='utf-8') as f:
        f.write(data4)
    print('successful to sign up')

# -------------------------------------------
# 拓拓展1.统计⽂文件中⼤大写字⺟母、⼩小写字⺟母、数字及其他字符出现的次数
# ⽂文件内容:Abc123,-+XYZopq000.?/
# 结果: {
# '⼤大写字⺟母': 4, '⼩小写字⺟母': 5, '数字': 6, '其他字符': 6
# }
# 分析:利利⽤用ASCII表，for循环遍历每⼀一个字符value，eg:'a' <= value <= 'z'就代表是⼩小写字 ⺟母
with open('3.txt', 'r', encoding='utf-8') as f:
    data = f.read()
dict_count = {'大写字母': 0, '小写字母': 0, '数字': 0, '其他字符': 0}
for i in data:
    if i.isalpha():
        if i.isupper():
            dict_count['大写字母'] += 1
        else:
            dict_count['小写字母'] += 1
    elif i.isnumeric():
        dict_count['数字'] += 1
    else:
        dict_count['其他字符'] += 1
print(dict_count)

# # 拓拓展2.完成登录注册系统(从空⽂文件开始做)
# # 需求分析:
# ''' 1.可以循环登录注册，输⼊入1代表选择登录功能，输⼊入2代表注册功能，输⼊入0代表退出，其他输⼊入代表 输⼊入有误，重输
# 2.⽤用户的账号密码信息存放在usr.txt⽂文件中，保证⽤用户注册成功后，重启系统，⽤用户信息仍然保存
# 3.登录在账号验证通过才输⼊入密码验证登录，账号验证三次失败⾃自动进⼊入注册功能，登录三次验证失败 ⾃自动退出系统
# 4.第⼀一次注册，⽂文件写⼊入 账号:密码 信息，再次注册追加写⼊入 |账号:密码 信息
# 分析过程:略略
import os


def sign():#1.注册
    print('*******signup********')
    username2 = input('username:')
    password2 = input('password:')
    with open('usr.txt', 'a', encoding='utf-8') as f:
        f.write('|' + username2 + ':' + password2)
    print('successful to signup')
    exit()


def login():#2.登录
    print('*******login*********')
    with open('usr.txt', 'r', encoding='utf-8') as f:
        data = f.read()
        usr_dict = {}
        for i in data.split("|"):
            k, v = i.split(":")
            usr_dict[k] = v
    count_num = 0
    while count_num < 3:
        username = input('username:')
        if username in usr_dict.keys():
            count_num2 = 0
            while count_num2 < 3:
                password = input('passord:')
                if password == usr_dict[username]:
                    print('successful to login')
                    exit()
                else:
                    count_num2 += 1
                    continue
            else:
                print('exit')
                exit()
        else:
            count_num += 1
            continue


def main():#3.主程序
    print('''
    help:
        1.登录
        2.注册
        0.退出''')
    if os.path.exists('usr.txt'):
        while True:
            user_choice = input('please input your choice:')
            if user_choice == '1':
                login()
            elif user_choice == '2':
                sign()
            elif user_choice == '0':
                exit()
            else:
                continue
    else:
        print('user not exist,please signup')
        print('*******signup********')
        username2 = input('username:')
        password2 = input('password:')
        with open('usr.txt', 'w', encoding='utf-8') as f:
            f.write(username2 + ':' + password2)
        print('successful to signup')


main()
