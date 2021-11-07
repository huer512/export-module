'''
Author: 兄弟们Go
Date: 2021-11-07 19:53:05
LastEditTime: 2021-11-07 20:36:48
LastEditors: 兄弟们Go
Description: 
FilePath: \pymodules\tests\test1.py

'''
from pymodules import *
j = require('dumps').From('json')
text = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]
print(j(text))
print(j)