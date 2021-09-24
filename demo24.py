
# 方法一
# a = 2.0
# b = 1.0
# s=0
# for n in range(1,21):
#     s += a/b
#     t=a
#     a=a+b
#     b=t
# print(s)


# 方法二
from functools import reduce
l=[]
a=2.0
b=1.0
for i in range(1,21):

    l.append(a/b)
    b, a = a, a + b
print(l)
print((reduce(lambda x,y:x+y,l)))