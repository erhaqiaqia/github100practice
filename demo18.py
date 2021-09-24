n = int(input("please input a geshu:"))
a = int(input("please input a num:"))

sum1=0
sum2=0
for count in range(n):
    b=pow(10,count)
    Tn = a*b
    sum1 += Tn
    sum2 += sum1
    print(sum1)
print(sum2)

