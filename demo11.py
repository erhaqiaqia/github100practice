# # 迭代法（斐波那契数列）
# def count(m):
#     if m == 1 or m == 2:
#         return 1
#     elif m > 2:
#         return count(m-2)+count(m-1)
#
# month = int(input("请输入月份:"))
# print(count(month))

# 循环
month = int(input("请输入月份:"))

first = 1
second = first

for i in range(1,month+1):
    if i==1 or i==2:
        new=1

    else:
       new =first+second
       second = first
       first = new

print(new)







