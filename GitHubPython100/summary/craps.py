# -*- coding: utf-8 -*- 
# @Time : 2021/9/23 13:43 
# @Author : cyt 
# @File : craps.py 
# @software: pycharm
"""
Craps赌博游戏
玩家摇两颗色子 如果第一次摇出7点或11点 玩家胜
如果摇出2点 3点 12点 庄家胜 其他情况游戏继续
玩家再次要色子 如果摇出7点 庄家胜
如果摇出第一次摇的点数 玩家胜
否则游戏继续 玩家继续摇色子
玩家进入游戏时有1000元的赌注 全部输光游戏结束

"""

from random import randint
money=1000
while money>0:
    print(f'你的总资产为{money}')
    while True:
        debt = int(input("请下注："))
        if debt > 0 and debt <= money:
            break
    needs_go_on = False
    first = randint(1,6) + randint(1,6)
    print(f"第一次转的点数{first}")
    if first == 7 or first == 11:
        print("玩家胜！")
        money += debt
    elif first==2 or first==3 or first==12:
        print("庄家胜！")
        money -= debt
    else:
        needs_go_on = True

    while needs_go_on:
        second = randint(1, 6) + randint(1, 6)
        if second == 7:
            print("庄家胜！")
            money -= debt
            needs_go_on=False
        elif second == first:
            print("玩家胜！")
            money += debt
            needs_go_on=False
print("你已坡长！")
