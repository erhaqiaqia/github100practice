
bonus1 = 100000 * 0.1
bonus2 = bonus1 + 100000*0.075
bonus4 = bonus2 + 200000*0.05
bonus6 = bonus4 + 200000*0.03
bouns10 = bonus6 + 400000*0.015
a = int(input("请输入当月利润i:"))
if a <=100000:
    bonus = a * 0.1
elif a<=200000:
    bonus = bonus1 + (a-100000)*0.075
elif a<=400000:
    bonus = bonus2 + (a-200000)*0.05
elif a<=600000:
    bonus = bonus4 + (a-400000) * 0.03
elif a<=1000000:
    bonus = bonus6 + (a-600000) * 0.015
else:
    bonus = bouns10 + (a-1000000) * 0.01

print('bonus=',bonus)
