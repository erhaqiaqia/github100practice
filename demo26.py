
# 利用递归求5的阶乘
def fact(j):
    suma=0
    if j==0:
        suma=1
    else:
        suma += j*fact(j-1)
    return suma

for i in range(6):
    print("%d != %d" %(i,fact(i)))