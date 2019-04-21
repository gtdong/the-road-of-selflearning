# -*- coding: utf-8 -*-
# 1.写出完整的装饰器器(不不⽤用考虑带参装饰器器，就是普通装饰器器)语法
def outer(func):
    def innner(*args, **kwargs):
        pass
        res = func(*args, **kwargs)
        pass
        return res

    return innner


@outer
def any_method():
    pass


# 2.有⼀一个计算两个数和的⽅方法，为其添加⼀一个确保两个参数都是int或float类型的装饰器器，保证运 算不不会抛异常
def check_type(func):
    def inner(num1, num2):
        if (isinstance(num1, int) or isinstance(num1, float)) and (isinstance(num2, int) or isinstance(num2, float)):
            res = func(num1, num2)
            return res
        return False

    return inner


@check_type
def sum(num1, num2):
    return num1 + num2


res = sum(1, 'a')
print(res)


# 3.有⼀一个⼀一次性录⼊入⼈人名并返回⼈人名的⽅方法(⼈人名只考虑存英⽂文)，为其添加⼀一个装饰器器，使得处理理 后⼈人名⾸首字⺟母⼀一定⼤大写
def big(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        res = result.capitalize()
        return res

    return inner


@big
def input_name():
    name = input("input your name:")
    return name


# res = input_name()
# print(res)

'''
 拓展题
1.原功能:entry_grade
*) 可以完成『成绩录⼊入功能』
-- 可以重复录⼊入成绩，默认所有输⼊入都是合法的(1~100之间的数)
-- 当录⼊入成绩为0时，结束成绩的录⼊入
-- 将录⼊入的成绩保存在列列表中并返回给外界，eg:[90, 80, 50, 70]
2.选择课程装饰器器:choose_course
*) 为『成绩录⼊入功能』新增选择课程的拓拓展功能，达到可以录⼊入不不同学科的成绩
-- 可以重复输⼊入要录制的学科名，然后就可以进⼊入该⻔门学科的『成绩录⼊入功能』，录⼊入结束后， 可以进⼊入下⼀一⻔门学科成绩录⼊入
-- 当输⼊入学科名为q时，结束所有录⼊入⼯工作
-- 将学科成绩保存在字典中并返回给外界，eg:{'math':[90, 80, 50, 70], 'english': [70, 50, 55, 90]}
3.处理理成绩装饰器器:deal_fail
*) 可以将所有录⼊入的成绩按60分为分⽔水岭，转换为 "通过" | "不不通过" 进⾏行行存储
-- 如果只对原功能装饰，结果还为list返回给外界，eg:["通过", "通过", "不不通过", "通 过"]
-- 如果对已被选择课程装饰器器装饰了了的原功能再装饰，结果就为dict返回给外界，eg: {'math':["通过", "通过", "不不通过", "通过"], 'english':["通过", "不不通过", "不不通过", "通过"]}
'''


def deal_fail(func):
    def inner(*args, **kwargs):
        res = func()
        tmp_dict = {}
        for k in res:
            tmp_list = []
            for l in res[k]:
                if l >= 60:
                    tmp_list.append('通过')
                    tmp_dict[k] = tmp_list
                else:
                    tmp_list.append('不通过')
                    tmp_dict[k] = tmp_list
        return tmp_dict
    return inner


def choose_course(func):
    def inner(*args, **kwargs):
        grade_dic = {}
        while True:
            subject = input("input the subject you want to input:")
            if subject == 'q':
                return grade_dic
            result = func()
            if subject in grade_dic:
                grade_dic[subject] += result
            else:
                grade_dic[subject] = result
            print(grade_dic)
        return grade_dic

    return inner

@deal_fail
@choose_course
def entry_grade():
    list_grade = []
    while True:
        grade = input("input your grade:")
        if int(grade) == 0:
            break
        list_grade.append(int(grade))
        print(list_grade)
    return list_grade


res = entry_grade()
print(res)
