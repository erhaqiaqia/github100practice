""""""

num=0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i!=j) and (i!=k) and (j!=k):
                print(i,j,k)
                num+=1
print("总共生成%d个数" %num )
