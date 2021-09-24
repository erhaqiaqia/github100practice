#定义一个二维列表
xh = []
number = int(input('请输入XH三角层数：'))
#外层循环控制层数
print("等腰杨辉三角")
for i in range(number):
	#每次循环前清空数据
    ls = []
    # PS: | 逻辑符号 两边对于数字类型必须得用'()'包起来，否则会进行数运行
    # 开头和结尾 都为 1
    if (i == 0):
        ls.append(1)
    else:
    	# 内存循环控制个数
        for j in range(i+1):
        	# 'or' 与 | 不同， 'or' 只为逻辑判断，所以不需要'()'
            if j == 0 or j == i:
                ls.append(1)
            else:
            	# 从二层开始，索引为n位置的值，为上一层索引为n-1位置和索引为n位置上值之和
                ls.append(xh[i-1][j-1] + xh[i-1][j])
    # 别忘了追加到二位列表中
    xh.append(ls)
    # 直角杨辉三角
    # print(ls)
    # 等腰杨辉三角    字符串有center函数，可以居中打印

    print(str(ls).center(number * 5))#域宽层数 * 5,两边填充空格
