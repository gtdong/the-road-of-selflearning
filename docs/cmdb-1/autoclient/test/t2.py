
import t1

# print(dir(t1))
for k in dir(t1):
    if k.isupper():
        print(k)
        v = getattr(t1, k)
        print(v)

