
class Student:
    name = '学生'
    def __init__(self, name, id_num):
        self.name = name
        self.id_num = id_num

    # 对象(成员)方法
    def study(self):  # 在类中产生的所有方法，都是属于类的，但是对象可以调用
        # print('self>>', id(self))
        print("%s在学习" % self.name)

    # 类方法: 第一个参数就是用来接收调用者，类方法的调用者一定是类，所以第一个参数命名约定为cls
    @classmethod
    def fn(cls):
        print(id(cls))


    # 静态方法
    @staticmethod
    def func():
        print('func run')


stu1 = Student('Bob', 1)
# print(stu1.__dict__)
# print(stu1.name)
# stu1.__dict__.clear()
# print(stu1.__dict__)
# print(stu1.name)

stu2 = Student('Tom', 2)

stu1.study()
# print(id(stu1))
stu2.study()
# print(id(stu2))

# 结论1：对象调用类中的方法，默认隐式将对象自身传入，在方法中，第一个参数用self来接受传入的对象


# Student.fn(Student) => Student.fn()
# print(id(Student))

Student.fn()
print(id(Student))

# 结论2：类中用@classmethod装饰的方法，是类方法，用类来调用，默认会将类传入给方法的第一个参数


Student.func()
stu1.func()
# 结论3：类中用@staticmethod装饰的方法，是静态方法，可以被类和对象调用，默认不会将类或对象传入

"""
# 总结：
# 1.对象方法对象调用，默认传入对象给第一个形参 
class 类名:
    def fn(self, *args, **kwargs): pass
    
# 2.类方法由类调用，默认传入类给第一个形参
class 类名:
    @classmethod
    def fn(cls, *args, **kwargs): pass
    
# 3.静态方法建议由类调用，默认不传入调用者
    @staticmethod
    def fn(*args, **kwargs): pass
"""

"""
在一个类中：何时何需求，会挑选何方法
"""
