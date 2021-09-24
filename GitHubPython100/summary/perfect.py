# -*- coding: utf-8 -*- 
# @Time : 2021/9/24 11:12 
# @Author : cyt 
# @File : perfect.py 
# @software: pycharm
"""
找出1~9999之间的所有完美数
完美数是除自身外其他所有因子的和正好等于这个数本身的数
例如: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14
"""

import math

for num in range(1, 10000):
    sum = 0
    for i in range(1, (num // 2)+1):
        if num % i == 0:
            sum += i
            # print(sum)
    if num == sum:
        print(num)


def fib(num):
    a=0
    b=1
    for i in range(20):
        (a,b)=(b,a+b)
        print(a,end=" ")
fib(20)