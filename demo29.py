x=int(input("输入一个数字：\n"))
a=x//10000
b=x%10000//1000
c=x%1000//100
d=x%100//10
e=x%10

if a != 0:
    print("there are 5:",e,d,c,b,a)


