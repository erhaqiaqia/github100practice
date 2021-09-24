while True:

    a = input("please input chars:")
    if a=='':
        print("ending")

        break
    letters,space,digit,others = 0,0,0,0
    for i in a:
        if i.isalpha():
            letters += 1
        elif i.isspace():
            space += 1
        elif i.isdigit():
            digit += 1
        else:
            others += 1
    print("这段话有%d个英文字母，%d个空格，%d个数字，%d个特殊符号" %(letters,space,digit,others))