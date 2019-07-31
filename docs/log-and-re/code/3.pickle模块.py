import pickle

# 序列化
obj = {'name': 'Owen', 'age': 17, 'gender': '男'}
res = pickle.dumps(obj)
print(res)

pickle.dump(obj, open('b.txt', 'wb'))


# 反序列化
print(pickle.loads(res))
print(pickle.load(open('b.txt', 'rb')))

