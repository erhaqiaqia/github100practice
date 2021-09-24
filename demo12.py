import math
# num = int(input("please input a number:"))
# if num == 1:
#     print("1不是素数")
# else:
total = 0
for i in range(101,201):
    for j in range(2,int(math.sqrt(i))+1):
        if i%j == 0:
            # print(str(i)+"不是素数")
            break
    else:
        print(str(i)+"是素数")
        total +=1
print(total)



