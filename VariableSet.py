
print('==========set operation===========')

a = {9,2,3,4}

print(len(a))
print(a)
#set 无顺序，无索引操作
# print(a[2])
# print(a.index(4))


#删除元素3
#a.remove(3)
a.pop()
print(a)

#增加元素5
a.add("5")
print(a)

#无重复元素验证，可以添加，但是会自动去重
a.add(2)
a.add('5123')
print(a)

#集合是无序的，多次打印可以看出它的元素顺序会变化。
#创建一个空集合
b = ()
print(type(b))