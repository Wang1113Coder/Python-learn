"""
演示判断语句的嵌套哈斯用
"""

# if int(input("请输入你的身高:"))>120:
#     print("身高超出限制,不可以免费")
#     print("但是如果VIP级别大于3,可以免费")
#
#     if int(input("你的VIP级别是多少:"))>3:
#         print("恭喜你,你的VIP级别达标,可以免费")
#     else:
#         print("sorry,你需要买票10元")
# else:
#     print("欢迎小朋友,免费游玩")


age=20
year=1
level=1
if age>=18:
    print("你是成年人")
    if age<30:
        print("你的年龄达标了")
        if year>2:
            print("恭喜你,年龄和入职时间都达标,可以领取礼物")
        elif level>3:
            print("恭喜你,年龄和级别达标,可以领取礼物")
        else:
            print("不好意思,尽管年龄达标,但是入职时间和级别都不达标")

    else:
        print("不好意思,年龄太大了")

else:
    print("不好意思,小朋友不可以领取")


