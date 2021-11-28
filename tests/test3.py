'''
Author: 兄弟们Go
Date: 2021-11-21 17:30:39
LastEditTime: 2021-11-28 15:57:20
LastEditors: 兄弟们Go
Description: 
FilePath: \pymodules\test3.py

'''
from pymodules import *
t2 = Import('test2').From("test2")
a = Import('a').From("test2")

# print(type(a).__name__)
# print(a.__IM__.__ImportData__["obj"])
# print(type(a.__IM__.__ImportData__["obj"]).__name__)
# print(t2)