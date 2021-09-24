n=0
t=1
for i in range(1,21):
    t *= i
    n += t
print("1!+2!+...+20!的值为%d" %n)
