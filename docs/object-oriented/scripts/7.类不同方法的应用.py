# 对象方法：方法的内部需要使用对象的数据，所以要传入对象
class Book:
    name = '书'
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # 书的详情信息 => 一定需要知道哪本书
    # @classmethod  # 类调用cls就是类，对象调用处理成 对象.__class__

    def detail(self):
        # print(cls.name)
        print("%s的价格为:%s元" % (self.name, self.price))

book1 = Book('西游记', 38.8)
book2 = Book('金瓶梅', 88.8)
book1.detail()
book2.detail()
# print(book1.__class__)


# 静态方法：方法的内部不需要对象及类的参与，所以定义为静态方法，但是方法必须由调用者，建议用类就可以了
class NumTool:  # 工具类 => 模块
    def max_two(self, n1, n2):
        max_num = n1 if n1 > n2 else n2
        print('大数是%s' % max_num)

    @staticmethod
    def new_max_two(n1, n2):
        max_num = n1 if n1 > n2 else n2
        print('大数是%s' % max_num)

n1 = NumTool()
n2 = NumTool()
n1.max_two(10, 20)
n2.max_two(10, 20)

NumTool.new_max_two(10, 20)
n1.new_max_two(10, 20)


# 类方法：方法的内部需要类的参与，所以定义为类方法，第一个参数默认传类
class NewNumTool:
    PI = 3.14

    @classmethod
    def new_max_two(cls, n1, n2):
        max_num = n1 if n1 > n2 else n2
        return max_num

    @classmethod
    def new_max_three(cls, n1, n2, n3):
        # max_num = "想去复用new_max_two"
        max_num = cls.new_max_two(n1, n2)
        max_num = cls.new_max_two(max_num, n3)
        return max_num

    @classmethod
    def is_PI(cls, num):
        if num == cls.PI:
            return True
        return False


res = NewNumTool.new_max_three(1, 5, 3)
print('大数是%s' % res)

print(NewNumTool.is_PI(3.149))