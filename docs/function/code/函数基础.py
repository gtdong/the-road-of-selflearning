# -*- coding: utf-8 -*-
# 1.定义⼀一个函数，该函数可以实现控制台输⼊入，最终返回⼀一个int类型的正整数 # 解析:如何将字符串串转换为int类型的正整数
def str_to_int():
    number = input('number:')
    try:
        return abs(int(number))
    except ValueError:
        print('输入错误,请输入数字')


# while True:
#     res = str_to_int()
#     print(res)


# 2.定义⼀一个函数，该函数可以实现⽤用户录⼊入，最终返回⼀一个int类型的负整数
# 解析:1.只能有⼀一个'-'且以它开头;2.按'-'拆分得到的⼀一定是⻓长度为2的列列表，且后⾯面的数是正整 数
def str_to_int1():
    num = input('number:')
    if num.isdigit():
        num = '-' + str(num)
        return int(num)
    elif num.startswith('-') and num.count('-') == 1:
        if num.split('-')[1].isdigit():
            return int(num)
    else:
        print('请输入正确的数字：')


# while True:
# res = str_to_int1()
# print(res)

# 3.定义⼀一个函数，实现传⼊入⼀一个数或是字符串串，返回值是 是否 是可转换为整数类型的数据 # 解析:运⽤用1，2的逻辑判断
def str_to_int2(num):
    # num = input('input:')
    if num.isdigit():
        return True
    elif num.startswith('-') and num.count('-') == 1:
        if num.split('-')[1].isdigit():
            return True
        else:
            return False
    else:
        return False


# while True:
#     res = str_to_int2()
#     print(res)


# 4.定义⼀一个函数，实现传⼊入⼀一个整型数字，判断并直接打印该数字是否是奇数还是偶数 # 解析:解决奇数、偶数的概念即可
def num_check(num):
    if int(num) % 2 == 0:
        return '偶数'
    else:
        return '奇数'


# res = num_check()
# print(res)


# 5.定义⼀一个函数，实现判断传⼊入数据的类型，并直接打印其类型 # 解析:如何判断数据的类型
def type_check(content):
    if isinstance(content, bool):
        print('bool')
    if isinstance(content, str):
        print('str')
    if isinstance(content, int):
        print('int')
    if isinstance(content, list):
        print('list')
    if isinstance(content, float):
        print('float')
    if isinstance(content, tuple):
        print('tuple')
    if isinstance(content, dict):
        print('dict')
    if isinstance(content, set):
        print('set')
    if isinstance(content, complex):
        print('complex')


ls = [1, '1', 3.14, True, [], {}, {1, }, (1,), 4 + 5j]
for v in ls:  # 丢进去各种功能，检测我们的功能是否能检查这些类型
    type_check(v)


# 6.定义⼀一个函数，实现可以重复录⼊入键盘信息，当⽤用户输⼊入q或Q时退出，否则判断是否为可转换为 整数类型的数据，可以的话输出该数是奇数还是偶数，否则直接输出该字符串串
# 解析:要调⽤用3，4题结果
def print_info():
    while True:
        num = input('num:')
        if num == 'q' or num == 'Q':
            break
        if str_to_int2(num):
            res = num_check(int(num))
            print(res)
        else:
            print(num)


# print_info()


# 7.定义⼀一个函数，只要传⼊入 "k1:v1,...,kn:vn" 格式的字符串串，都可以将其转换为 {'k1':'v1',...,'kn':'vn'}
# 解析:字符串串拆分与for循环迭代
def to_dict(data):
    dic = {}
    data_list = data.split(',')
    for i in data_list:
        k, v = i.split(':')
        dic[k] = v

    print(dic)


to_dict("k1:v1,kn:vn")

# 8.定义⼀一个函数，实现列列表与元组类型的反转功能 # 解析:传⼊入列列表返回元组，传⼊入元组返回列列表
def list_to_tuple(data):
    if isinstance(data,list):
        return tuple(data)
    if isinstance(data,tuple):
        return list(data)
res = list_to_tuple((1,2))
res2 = list_to_tuple([1,2])
print(res)
print(res2)
# 9.定义⼀一个函数，可以完成对list、tuple、dict、set四种类型数据的循环变量量打印，不不是这四 种，则打印 "暂不不⽀支持该数据遍历"
# 解析:对数据类型做判断
def type_print(data):
    if isinstance(data,list) or isinstance(data,tuple) or isinstance(data,set):
        for i in data:
            print(data)
    if isinstance(data, dict):
        for k, v in data.items():
            print(k, v)
    else:
        print("暂不不⽀支持该数据遍历")
# 10.定义⼀一个函数，实现对单列列集合进⾏行行去重的功能
# 解析:单列列集合有list、tuple、set，传⼊入list、tuple、set，返回去重后的list、tuple、 set，考虑可变与不不可变类型的不不同处理理
def remove_duplicates(data):
    list_data = []
    if isinstance(data,list):
        for l in data:
            if l not in list_data:
                list_data.append(l)
        return list_data
    if isinstance(data,tuple):
        for t in data:
            if t not in list_data:
                list_data.append(t)
        return tuple(list_data)
    if isinstance(data,set):
        return data
print(remove_duplicates([1,2,2,3]))
print(remove_duplicates((1,2,2)))
print(remove_duplicates({1,2,2,3}))


# 11.定义⼀一个函数，实现⽂文件(不不⼀一定是⽂文本⽂文件)的跨⽂文件夹的裁剪
# 解析:1.传⼊入要读取的⽬目标⽂文件夹中的⽬目标⽂文件;2.在被告知的⽬目标⽂文件夹下复制成同名⽂文件;3.调 ⽤用os中删除⽂文件的功能将原⽂文件删除
import os
def file_move(file,path):
    filename = file.rsplit('/',1)[1]
    to_path = path + filename
    with open(file,'r',encoding='utf-8') as f:
        data = f.read()
        with open(to_path,'w') as f2:
            f2.write(data)
    os.remove(file)

# file_move('/Users/dgt/python3_learning/day4_0414/董国涛-week4/1.txt','/Users/dgt/python3_learning/day4_0414/day04/')
# 拓拓展1:⽤用函数实现判断⼀一个字符串串数据能否转换为正负⼩小数
# 先考虑正⼩小数，再在基础上考虑负⼩小数，可以形成多个⽅方法，形成函数的嵌套
# 正⼩小数:只包含⼀一个⼩小数点，左右都是正整数
# 负⼩小数:参考普通题的第2题结合正⼩小数
# ⼀一个.，按.拆分的左右都是数字
# "-"开头，刨除"-"后是正整数
def is_demical(num):
    if num.count('.') == 1:
        str1 = str(num)
        s = str1.split('.')
        left = s[0]
        right = s[1]
        if left.isdigit() and right.isdigit():
            return True
        elif left.startswith('-') and left.count('-') == 1 and right.isdigit():
            lleft = left.split('-')[1]
            if lleft.isdigit():
                return True
    return False


def is_demical_main(num):
    if isinstance(num,str):
        res = is_demical(num)
        return res
    else:
        print('类型输入错误，请重新输入')
print(is_demical_main('-b0.122b'))



# 拓拓展2:实现汽⻋车销售系统
'''
1)具有进货功能1，销售⻋车辆功能2，展示所有库存功能3，展示销售总业绩功能4 2)⽤用户输⼊入0退出系统，输⼊入提供的功能编号，完成对应的功能，否则重新输⼊入，eg:2就进⼊入销售⻋车 功能
3)⻋车辆信息具有持久化(⽂文件永久)存储功能，⻋车辆有奔驰|宝⻢马|奥迪三款
⽂文件信息:
total.txt: 就是记录了了总销售额
car.txt: 宝⻢马 120000 9 奔驰 150000 7 奥迪 100000 8
4)进货功能:选择进货的⻋车型与数量量，完成进货 5)售⻋车功能:选择售出的⻋车，有库存售出，更更新销售总业绩，没有则进⼊入进货功能 6)展示库存:显示所有⻋车与库存两条信息即可
7)总业绩:显示总业绩⾦金金额即可
分析:要将total.txt与car.txt转换为合适的数据类型，操作完毕后同步到⽂文件中即可 '''


def load_car_information():
    with open('car.txt', 'r', encoding='utf-8') as f:
        car_data = f.read()
    car_dict1 = eval(car_data)
    return car_dict1


def load_total_information():
    with open('total.txt', 'r', encoding='utf-8') as f:
        total_amount = f.read()
    return total_amount


def stock_goods():
    dict_res = load_car_information()
    print(dict_res)
    print('''
    1:宝马
    2:奥迪
    3:奔驰
    ''')
    car_models = input("input your models of cars:")
    stock_number = input("input number to stock:")
    dict_res[car_models]['number'] += int(stock_number)
    print(dict_res)
    with open('car.txt', 'w', encoding='utf-8') as f:
        f.write(str(dict_res))


def cars_sale():
    print('''
    1: 宝马
    2: 奥迪
    3: 奔驰
    ''')
    car_models = input("input your models of cars to sell:")
    dict_res = load_car_information()
    if dict_res[car_models]['number'] > 0:
        dict_res[car_models]['number'] -= 1
        with open('car.txt', 'w', encoding='utf-8') as f:
            f.write(str(dict_res))
        total_amount = load_total_information()
        total_amount = str(int(total_amount) + dict_res[car_models]['price'])
        with open('total.txt', 'w', encoding='utf-8') as f:
            f.write(total_amount)
    else:
        stock_goods()


def display_inventory():
    dict_res = load_car_information()
    for k in dict_res:
        print(k, ':', dict_res[k]['number'])


def display_sale():
    total_res = load_total_information()
    print(total_res)


def main():
    while True:
        print('''
        1:进货功能
        2:销售车辆功能
        3:展示所有库存功能
        4:展示销售业绩
        0:退出''')
        user_choice = input("input your choice:")
        if user_choice == '1':
            stock_goods()
        elif user_choice == '2':
            cars_sale()
        elif user_choice == '3':
            display_inventory()
        elif user_choice == '4':
            display_sale()
        elif user_choice == '0':
            break
        else:
            print('wrong input,pelase input the rigth number!')

# if __name__ == '__main__':
# main()
