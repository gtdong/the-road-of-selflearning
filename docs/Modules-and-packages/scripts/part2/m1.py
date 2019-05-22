# print('begin')

price = 12000  # ②

def t1():
    print(price)  # 访问②当前文件的全局名称空间中的price
    print('t1 功能')

def t2():
    print('t1 功能')

def t3():
    print('t1 功能')
# print('end')


