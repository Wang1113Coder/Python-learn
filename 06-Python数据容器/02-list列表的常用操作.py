"""
演示数据容器之:list列表的常用操作
"""
my_list=["itcast","itheima","Python"]
# 1.1查找某元素在列表内的下标索引
index=my_list.index("itheima")
print(f"itheima在列表中的下标索引值是:{index}")
# 1.2如果被查找的元素不存在,会报错
# index=my_list.index("hello")
# print(f"itheima在列表中的下标索引值是:{index}")

# 2.修改特定下表索引的值
my_list[0]="传智教育"
print(f"列表被修改元素后,结果是:{my_list}")
# 3.在指定下标位置插入新元素
my_list.insert(1,"best")
print(f"列表插入元素后,结果是:{my_list}")
# 4.在列表的尾部追加单个新元素
my_list.append("黑马程序员")
print(f"列表在追加了元素后,结果是:{my_list}")
# 5.在列表的尾部追加一批新元素
my_list2=[1,2,3]
my_list.extend(my_list2)
print(f"列表再追加了一个新的列表后,结果是:{my_list}")
# 6.删除制定下标索引的元素(两种方式)
my_list=["itcast","itheima","Python"]

# 6.1 方式1:del 列表[下标]
del my_list[2]
print(f"列表删除元素后结果是:{my_list}")
# 6.2 方式2:列表.pop(下标)
my_list=["itcast","itheima","Python"]
element=my_list.pop(2)
print(f"通过pop方法取出元素后列表内容:{my_list},取出的内容是:{element}")
# 7.删除某元素在列表中的第一个匹配项
my_list=["itcast","itheima","itcast","itheima","Python"]
my_list.remove("itheima")
print(f"通过remove方法移除元素后,列表的结果是:{my_list}")

# 8.清空列表
my_list.clear()
print(f"列表被清空了,结果是:{my_list}")
# 9.统计列表内某元素的数量
my_list=["itcast","itheima","itcast","itheima","Python"]
count=my_list.count("itheima")
print(f"列表中itheima的数量是:{count}")

# 10.统计列表中全部的元素数量
my_list=["itcast","itheima","itcast","itheima","Python"]
count=len(my_list)
print(f"列表的元素数量总共有:{count}个")

