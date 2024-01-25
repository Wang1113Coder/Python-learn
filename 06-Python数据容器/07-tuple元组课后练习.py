"""
定义一个元组,内容是("周杰伦",11,["football","music"])
1.查询其年龄所在的下标位置
2.查询学生姓名
3.删除学生爱好中的football
4.增加爱好:coding到爱好list内
"""
t1=("周杰伦",11,["football","music"])
num=t1.index(11)
print(f"年龄所在下标为:{num}")
print(f"学生姓名为:{t1[0]}")
del t1[2][0]
print(f"删除爱好后结果是:{t1}")
t1[2].insert(0,"coding")
print(f"增加爱好后结果是:{t1}")


