import math
for i in range(100000):
    x=int(math.sqrt(100+i))
    y=int(math.sqrt(268+i))
    if (x*x == 100+i)and(y*y == 268+i):
        print(i)