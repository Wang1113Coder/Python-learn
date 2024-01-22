"""
定义一个数字变量num
使用range语句获取从1到num的序列,使用for循环遍历
统计有多少个偶数出现
"""
num=range(1,100)
count=0
for x in num:
    if x%2==0:
        count+=1
print(f"从1-100(不包含100本身)范围内,有{count}个偶数")

