"""
演示if elif else练习题:猜测心里数字
"""

# 定义一个变量数字
num=5

# 通过键盘输入获取猜想的数字,通过多次if elif else的组合进行猜想比较
if int(input("请猜一个数字:"))==num:
    print("恭喜,第一次就猜对了")
elif int(input("猜错了,再猜一次:"))==num:
    print("猜对了")
elif int(input("猜错了,再猜一次:"))==num:
    print("恭喜,最后一次机会猜对了")
else:
    print("sorry,猜错了")

