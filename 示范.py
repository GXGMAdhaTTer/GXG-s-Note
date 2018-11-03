# -*- coding: utf-8 -*-

# from functools import reduce


# def str2float(s):
#     sArr = s.split('.')
#     leng = len(sArr[1])
#     t = 1.0
#     while leng > 0:
#         t*=10
#         leng-=1
#     L = list(map(float,sArr))
#     return [L[0]+L[1]/t]


# print('str2float(\'123.456\') =', str2float('123.456'))

# def count():
#     fs = []
#     for i in range(1,4):
#         def f():
#             return i*i
#         fs.append(f)
#     return fs
# f1, f2, f3, f4 = count()
# print(f4())

# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper


# @log
# def now():
#     print('2015-3-25')


# now()

# def int2(x,base = 2):
#     return int(x,base)

# import functools
# int2 = functools.partial(int, base=2)
# print(int2('1000000'))

# dec = int(input("输入数字："))
 
# print("十进制数为：", dec)
# print("转换为二进制为：", bin(dec))
# print("转换为八进制为：", oct(dec))
# print("转换为十六进制为：", hex(dec))

# 'a test module'

# __author__ = 'GXG'

# import sys

# def test():
#     args = sys.argv
#     if len(args)==1:
#         print('Hello, world!')
#     elif len(args)==2:
#         print('Hello, %s' %args[1])
#     else:
#         print('Too many arguments!')

# if __name__=='__main__':
#     test()

class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' %(self.name, self.score))

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)

bart.print_score()
lisa.print_score()