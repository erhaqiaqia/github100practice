# -*- coding: utf-8 -*- 
# @Time : 2021/9/23 15:01 
# @Author : cyt 
# @File : fibonacci.py 
# @software: pycharm
"""
输出斐波那契数列的前20个数
1 1 2 3 5 8 13 21 ...
"""


def fibo(num):
    a = 1
    b = 1
    for _ in range(20):
        (a, b) = (b, a + b)
        print(a, end=" ")


fibo(20)
print()


def fibo1(num):
    if num == 1 or num == 2:
        return 1
    else:
        return fibo1(num - 1) + fibo1(num - 2)


for i in range(1, 21):
    print(fibo1(i),end=" ")
