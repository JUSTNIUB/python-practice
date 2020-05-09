
print("===========list 操作=============")
a = [1,2,3,4]
print(len(a))
print(a[2])

#修改第3个元素为5
a[2] = 5
print("modify:",a)
#删除第3个元素
# del a[2]
a.remove(a[2])
print("del:",a)

#向尾部添加一个元素
a.append('a')
print("add element:",a)

#在第2个元素前插入一个元素7
a.insert(1,'c')
print("insert element:",a)

#将另一个集合添加到尾部
a.extend([[1,2],3,4,5])
print("extend:",a)
#查看元素7的索引
print("index:",a.index('c'))

a.remove('c')
a.remove('a')
del a[3]
print("pop",a)

#排序
a.sort()
#正序
print(a)
#反序
a.sort(reverse=True)
print(a)

#清空元素
a.clear()
print(a)
