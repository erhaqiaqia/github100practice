def age(i):
    if i==1 :
        n=10
    else:
        n = 2 + age(i-1)

    return n

print(age(5))