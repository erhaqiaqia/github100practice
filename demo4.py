year=int(input("请输入年份："))
month = int(input("请输入月份："))
day = int(input("请输入天数："))
# 闰年状态下的天数
list=[31,60,91,121,152,182,213,244,274,305,335,366]
if month>=1 and month <=12:
    if month == 1:
        count = day

    if month == 2:
        count=day+31

    if(year % 4 == 0 and year % 100 == 0) or (year % 400 == 0):
        if month>2 and month<=12:
            count = list[month-2]+day

    else:
        count = list[month - 2] + day-1

print("这是今年的第%d天" %count)





