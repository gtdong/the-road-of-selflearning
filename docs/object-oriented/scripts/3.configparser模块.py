import configparser

# 1.初始化
parser = configparser.ConfigParser()

# 2.读
parser.read('my.ini', encoding='utf-8')
# section | option | value
sts = parser.sections()
print(sts, type(sts))  # ['server', 'client'] <class 'list'>
ops = parser.options(sts[0])
print(ops)  # ['ip', 'port']
value = parser.get(sts[0], ops[0])
print(value, type(value))
# get=>str getboolean=>bool getfloat=>float getint=>int
print(parser.get('server', 'port'))

# 3.写
parser.read('my.ini', encoding='utf-8')
parser.set('server', 'port', '6666')
parser.write(open('my.ini', 'w'))
