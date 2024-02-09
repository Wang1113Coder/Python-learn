"""
演示类和对象的关系:即面向对象的编程套路(思想)
"""

# 设计一个闹钟类
class Clock:
    id=None # 序列号
    price=None # 成员价格


    def ring(self):
        import winsound
        winsound.Beep(2000,3000)

# 构建两个闹钟对象并让其工作
clock1=Clock()
clock1.id="003032"
clock1.price=19.99
print(f"闹钟ID:{clock1.id},价格:{clock1.price}")
clock1.ring()

clock2=Clock()
clock2.id="003032"
clock2.price=19.99
print(f"闹钟ID:{clock2.id},价格:{clock2.price}")
clock2.ring()
