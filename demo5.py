l=[]
for i in range(3):
    print(i,end = ' ')
    num = int(input("please input your num:"))
    l.append(num)

l.sort()
print(l)