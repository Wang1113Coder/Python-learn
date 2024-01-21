"""
演示if else练习题:我要买票吗
"""

# 定义键盘输入,获取身高数据
height=int(input("请输入您的身高(cm):"))

# 通过if进行判断
if height>120:
    print("您的身高超出120cm,需要买票10元钱")
else:
    print("您的身高低于120cm,可以免费游玩")

print("祝您游玩愉快")

