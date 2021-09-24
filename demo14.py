# num = int(input("输入一个数："))
# #因为输出格式中不存在空格，所以我把打印分开写了
# print(num, end='')
# print('=', end='')
# i = 1
# #用for循环的话是不能改变循环次数的，如果要改变循环次数的话最好用while。
# while i <= num + 1:
#     #通过判断余数是否为0，得出是否能整除
#     mid = num % i
#     if mid == 0:
#         print(i, end='')
#         #python经过除法后默认把类型转为浮点，所以为了保险，强制类型转换为int
#         num = int(num / i)
#         i = 1
#         #为了控制输出的乘号，加了一个判断条件，当num为1时说明没有质子了
#         if num != 1:
#             print('*', end='')
#     i += 1




# while 1:
#     n = int(input('请输入一个整数：'))
#     print('%d='%n,end='')
#     while n>1:
#         for i in range(2,n+1):
#             if n%i==0:
#                 n=int(n/i)
#                 if n==1:
#                     print('%d'%i,end='')
#                 else:
#                     print('%d*'%i,end='')
#                 break
#     print()






import random
# x = random.random()
# print(x)
# random.seed(10)  #复用伪随机数
# print(random.random())
# print(random.random())
# random.seed(10)
# print(random.random())


# a = [1,2,3]
# b = ['e','f','g']
# c = zip(a,b)
# # print(list(c))
# d = zip(*c)
# print(list(d))
