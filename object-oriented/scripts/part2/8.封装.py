
class Worker:
    # 在类中，不管是类属性方法，还是对象属性方法，还是静态方法
    # 只要是通过 __名字 这种命名规范，就是对外隐藏
    # 本质：__名字 封装隐藏变量的本质是 将名字修饰成 _类名__名字
    __a = '类的属性'
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    @classmethod
    def __b(cls):
        print("类的方法")

    def __c(self):
        print('对象的方法')

    @staticmethod
    def __d():
        print('静态方法')

# 入职offer
w1 = Worker('Owen', 88888)
w2 = Worker('P7', 222222222)

# 需求：再次访问，工资应该需要对外隐藏
# print(w1.name, w1.salary)
# print(w2.name, w2.salary)

# print(w1.__salary)
# print(Worker.__a)
# print(Worker.__b)
# print(w1.__c)
# print(Worker.__d)
# print(Worker._Worker__b)
# print(Worker.__dict__)

# 总结：Python中对变量的隐藏是伪隐藏，本质就是变量名的变形 __名字 => _类名__名字


# 隐藏并不是最终目的，添加访问权限才是隐藏的真正目的

class Test:
    def __init__(self, name):
        # __name只是对外隐藏，对内可见
        self.__name = name

    def test(self):
        print('test run, name: %s' % self.__name)  # 可以直接访问__开头的名字

    # 名字封装，只是想让外界不能直接通过名字使用名字
    # 1.如果真的不想让外界访问，就不对外提供访问数据的方法
    # 2.如果想让外界访问，可以对外提供访问数据的方法，方法具有逻辑，使用可以添加操作权限
    def get_name(self):
        return self.__name

    def set_name(self, name):
        if 'sb' not in name:  # 对数据的修改可能会产生数据的安全性问题，可以添加限制条件
            self.__name = name


t1 = Test('t1')
t1.test()
Test('t2').test()


print(t1.get_name())
t1.set_name('tt1')
print(t1.get_name())

t1.set_name('sb t1')
print(t1.get_name())

# python提供
# 优化：对象.get_名字() => 对象.名字
# 优化：对象.set_名字(new_value) => 对象.名字 = new_value


class User:
    def __init__(self, name):
        self.__name = name

    @property  # 将方法伪装成属性
    def name(self):
        return self.__name

    @name.setter  # 能为有伪装get方法的(方法)属性，再伪装set方法
    def name(self, value):
        self.__name = value

    @name.deleter
    def name(self):
        del self.__name
        # pass

    @property
    def pwd(self):
        return '123456'

u1 = User('Owen')
print(u1.name)  # 如果一个方法伪装成属性，对象.方法名 就会自动调用该方法

# u1.name = 'Zero'
# print(u1.name)

# del u1.name
# print(u1.name)

# print(u1.pwd)