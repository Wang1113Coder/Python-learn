"""
定义一个元组,内容是('周杰伦',11,["football","music"])
"""
t1=('周杰伦',11,["football","music"])

# 1.查询其年龄所在的下标位置
num=t1.index(11)
print(f"年龄所在的下标位置是:{num}")

# 2.查询学生的姓名
name=t1[0]
print(f"学生的姓名是:{name}")

# 3.删除学生爱好中的football
del t1[2][0]
print(f"删除后的学生信息是:{t1}")

#4.增加爱好coding到爱好list中
t1[2].append("coding")
print(f"增加爱好后学生的信息是:{t1}")