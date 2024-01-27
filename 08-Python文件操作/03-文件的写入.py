"""
演示文件的写入
"""
import time

# 打开文件,不存在的文件

# f=open("D:/学习/python/code/08-Python文件操作/test.txt","w",encoding="UTF-8")
# # write写入
# f.write("Hello world!!!") # 内容写到内存中
# # flush刷新
# f.flush() # 将内存中积攒的内容写入到硬盘的文件中
# # close关闭
# f.close() # close方法是内置了flush功能的
# 打开一个存在的文件
f=open("D:/学习/python/code/08-Python文件操作/test.txt","w",encoding="UTF-8")
# write写入,flush刷新
f.write("黑马程序员")
# close关闭
f.close()

