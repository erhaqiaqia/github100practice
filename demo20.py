high = 100
sum = 0
for i in range(1,11):
    a=high/2
    print("每次落下的反跳回的高度:",a)
    sum +=a
    high=a
print(sum)