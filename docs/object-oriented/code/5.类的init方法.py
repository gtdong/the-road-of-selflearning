
class Teacher:
    name = '教授'

def set_obj(obj, name, sex, age):
    obj.name = name
    obj.sex = sex
    obj.age = age

t1 = Teacher()
# t1.name = '苍老师'
# t1.sex = "女"
# t1.age = 36
set_obj(t1, '苍老师', "女", 36)
print(t1.name, t1.sex, t1.age)

t2 = Teacher()  # 类()应该就是函数的调用，函数调用可以传参，能优化属性的赋值
# t2.name = '武老师'
# t2.sex = "女"
# t2.age = 28
set_obj(t2, '武老师', "女", 28)
print(t2.name, t2.sex, t2.age)

# t3 = Teacher()
# set_obj(t3, '王大锤', '男', 58)

# 能不能再优化 => t3 = Teacher('王大锤', '男', 58)
# print(t3.name, t3.sex, t3.age)


class NewTeacher:
    def __init__(obj, name, sex, age):
        # print(id(self))
        # print('init 被调用了')
        obj.name = name
        obj.sex = sex
        obj.age = age
    pass

# 类()就是在调用类的__init__方法
nt1 = NewTeacher('王大锤', '男', 58)
# print(id(nt1))
print(nt1.name, nt1.sex, nt1.age)




