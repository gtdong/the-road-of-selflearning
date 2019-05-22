# 递归：函数直接或间接调用自己
# 回溯：找寻答案的过程
# 递推：通过最终的值反向一步步推出最初需要的结果

# count = 1
# age = 58
# while count < 2:
#     age -= 2
#     count += 1
# print(age)

# import sys
# print(sys.getrecursionlimit())  # 最大递归层 1000
# sys.setrecursionlimit(100)

# count = 0
# def a():
#     global count
#     print(count)
#     count += 1
#     a()
# a()

# def b():
#     d()
#
# def c():
#     b()
#
# def d():
#     c()
# d()


# 拿递归求得年纪
def get_age(num):
    if num == 1:
        return 58
    age = get_age(num - 1) - 2
    return age
age = get_age(10)
print(age)

# 前提：
# 1.递归条件是有规律的
# 2.递归必须有出口

# 传入一个num，求得该num的阶乘
# 5! = 5 * 4 * 3 * 2 * 1 = 5 * 4!
# 4! = 4 * 3 * 2 * 1 = 4 * 3!
# 3! = 3 * 2 * 1 = 3 * 2!
# 2! = 2 * 1 = 2 * 1!
# 1! = 1
def get_total(num):
    if num == 1 or num == 0:
        return 1
    total = num * get_total(num - 1)  # 3 * 2! => 2 * 1!1 => 1 => 2 * 1
    return total
print(get_total(3))






