from django.test import TestCase

# Create your tests here.
l=[2,4,5,6,7]
for i in l:
    if i%2==0:
        l.remove(i)
print(l)