"""
设计一个类,记录学生的:姓名,年龄,地址
通过for循环,配合input输入语句,并使用构造方法,完成学生信息的键盘录入
驶入完成后,使用print语句,完成信息输出
"""
class check_in():
    name=None
    age=None
    add=None
    def __init__(self,name,age,add):
        self.name=name
        self.age=age
        self.add=add
for i in range(1,10):
    print(f"当前录入第{i}位学生信息,总共需录入10位学生信息")
    stu=check_in(input("请输入你的姓名:"),input("请输入你的年龄:"),input("请输入你的地址:"))
    print(f"学生{i}信息录入完成,信息为:学生姓名:{stu.name},年龄:{stu.age},地址为:{stu.add}")