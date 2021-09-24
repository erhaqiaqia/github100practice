a=[9,5,6,7,23425,674,7,8,9]
print(len(a))
print(a)
for i in range(len(a)//2):
        a[i],a[-i-1] = a[-i-1],a[i]
print(a)