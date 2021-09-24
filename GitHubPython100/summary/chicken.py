# -*- coding: utf-8 -*- 
# @Time : 2021/9/23 11:13 
# @Author : cyt 
# @File : chicken.py 
# @software: pycharm
"""
求解《百钱百鸡》问题
1只公鸡5元 1只母鸡3元 3只小鸡1元 用100元买100只鸡
问公鸡 母鸡 小鸡各有多少只
"""

for x in range(20):
    for y in range(33):
        z = 100 - x - y
        if 5 * x + y * 3 + z / 3 == 100:
            print(f'{x},{y},{z}')
