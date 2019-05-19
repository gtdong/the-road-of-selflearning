'''
(0, 1)：random.random()
[1, 10]：random.randint(1, 10)
[1, 10)：random.randrange(1, 10)
(1, 10)：random.uniform(1, 10)
单例集合随机选择1个：random.choice(item)
单例集合随机选择n个：random.sample(item, n)
洗牌单列集合：random.shuffle(item)
'''
import random
print(random)

# for i in range(10):
#     print(random.random())  # (0, 1)


# for i in range(10):
#     print(random.randint(1, 10))  # [1, 10]

# for i in range(10):
#     print(random.randrange(1, 10))  # [1, 9]  [1, 10)

for i in range(10):
    print('%.2f' % random.uniform(1, 10))  # 小数：(1, 10)


ls = [1, 2, 3, 4, 5]
print(random.shuffle(ls))
print(ls)

print(random.choice(ls))

print(random.sample(ls, 3))


# 验证码
def get_code(count):
    code = ""
    # 能产生大小写字母与数字
    # 进行字符串拼接
    for i in range(count):
        c1 = chr(random.randint(65, 90))
        c2 = chr(random.randint(97, 122))
        c3 = str(random.randint(0, 9))
        code += random.choice([c1, c2, c3])
    return code

print(get_code(18))



def get_code(count):
    code = ""
    # 能产生大小写字母与数字
    # 进行字符串拼接
    for i in range(count):
        r = random.choice([1, 2, 3])
        if r == 1:
            c = chr(random.randint(65, 90))
        elif r == 2:
            c = chr(random.randint(97, 122))
        else:
            c = str(random.randint(0, 9))
        code += c
    return code
print(get_code(18))


def get_code(count):
    target = "1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
    code_list = random.sample(target, count)
    return ''.join(code_list)

print(get_code(6))


