from math import sqrt
ss=[]
for i in range(2,100):
    for j in range(2,i):
        if i % j == 0:
            print("%d 不是素数" %i)
            break
    else:
        ss.append(i)

print(ss)
