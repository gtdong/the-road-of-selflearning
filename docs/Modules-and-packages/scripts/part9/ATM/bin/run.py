import sys
# sys.path.append(r'D:\python周末四期\week6_0427\代码\part9\ATM')
# print(__file__)
import os
# path = os.path.dirname(os.path.dirname(__file__))
# print(path)
sys.path.append(os.path.dirname(os.path.dirname(__file__)))


from db import db_handle
print(db_handle)