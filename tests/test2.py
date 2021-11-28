'''
Author: 兄弟们Go
Date: 2021-11-21 15:17:33
LastEditTime: 2021-11-21 19:03:52
LastEditors: 兄弟们Go
Description: 
FilePath: \pymodules\test2.py

'''
# import inspect
from pymodules import *
def test2(name):
    print(name)
class a(object):
    def __init__(self):
        pass
Export(test2,a)