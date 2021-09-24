a=[29, 37, 38, 39, 40, 42, 64, 65, 70, 83]
print(len(a))
x = int(input("please input a number:"))


if x>a[-1]:
    a.append(x)
else:
    for i in range(len(a)):
        if a[i]>x:
            a.insert(i,x)
            break

print(a)