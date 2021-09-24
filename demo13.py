import math
for i in range(100,1000):
    x = i//100
    y = i%100//10
    z = i%10
    a = math.pow(x,3)
    b = math.pow(y,3)
    c = math.pow(z,3)
    if a+b+c == i:
        print(i,end=" ")

