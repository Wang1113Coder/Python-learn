"""
演示判断语句的是实战案例:终极猜数字
"""

# 1.构建一个随机的数字变量
import random
num=random.randint(1,10)

guess_num=int(input("输入你要猜测的数:"))

# 2.通过if判断语句进行数字的猜测
if guess_num==num:
    print("恭喜你,第一次就猜中了")
else:
    if guess_num>num:
        print("猜大了")
    else:
        print("猜小了")

    guess_num = int(input("再次输入你要猜测的数:"))

    if guess_num==num:
        print("恭喜你,第二次猜中了")
    else:
        if guess_num>num:
            print("猜大了")
        else:
            print("猜小了")

        guess_num = int(input("再次输入你要猜测的数:"))

        if guess_num==num:
            print("第三次猜中了")
        else:
            print("三次机会用完了,没有猜中")


