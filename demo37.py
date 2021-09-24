import random

# qz = []
# 随机取10个数字（有可能相同）
# for i in range(10):
#     a = random.randint(1,100)
#     qz.append(a)
# print(qz)

# 随机生成10个不同的数字
# result = random.sample(range(1,100),10)
# print(result)

# 第二种：随机生成10个不同的数字
result=[]
while len(result)<10:
    for i in range(10):
        a = random.randint(1,100)
        if a not in result:
            result.append(a)
print(result)
# 排序
# result.sort(reverse=True)
# print(result)
b=[]
num = 0
for i in range(len(result)):
    for j in range(i+1,len(result)):
        if result[i]>result[j]:
            result[i],result[j] = result[j],result[i]
    num +=1
    print("第%d次排序："%num,end="" )
    print(result)

print("排序后：",result)




