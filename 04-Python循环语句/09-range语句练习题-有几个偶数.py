"""
定义一个数字变量num,使用range语句
获取从1到num的序列,使用for循环遍历
统计有多少个偶数出现
"""
count=0
for x in range(1,100):
    if x%2==0:
        count+=1
print(f"1-100(不含100本身)中一共有{count}个偶数")
