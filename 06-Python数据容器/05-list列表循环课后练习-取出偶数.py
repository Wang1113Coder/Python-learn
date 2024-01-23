"""
定义一个列表,内容是[1,2,3,4,5,6,7,8,9,10]
遍历列表,取出列表内的偶数,存入一个新的列表对象中
使用while循环和for循环各操作一次
"""
my_list=[1,2,3,4,5,6,7,8,9,10]

# while
index=0
my_list2=list()
while index<len(my_list):
    if my_list[index]%2==0:
        my_list2.append(my_list[index])
    index+=1
print(my_list2)

# for
my_list2=list()
for element in my_list:
    if element%2==0:
        my_list2.append(element)
print(my_list2)
