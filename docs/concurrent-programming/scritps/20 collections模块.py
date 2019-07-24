from collections import namedtuple
# 具名元组  (具有名字的元组)
# a = (1,2)
# # p = namedtuple('坐标',['x','y'])
# p = namedtuple('坐标','x y z')
# location1 = p(1,2,3)  # 元素的个数一定要跟上面第二个参数的个数相同
# print(location1)
# print(location1.x)
# print(location1.y)
# print(location1.z)
# card = namedtuple('扑克牌',['color','number'])
# A = card('♠','A')
# print(A)
# print(A.color)
# print(A.number)

# city = namedtuple('日本',['countryname','name','gender','size'])
# c = city('东京','冲老师','female','L')
# print(c)

#
# from collections import deque
# """
# append
# appendleft
#
# pop
# popleft
# """
# q = deque()
# q.append(1)
# q.appendleft(2)
# print(q.pop())
# print(q.popleft())
# print(q)
# from collections import Counter
# res = 'abcdeabcdabcaba'
# res1 = Counter(res)
# print(res1.get('a'))
