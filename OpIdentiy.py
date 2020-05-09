import copy

print("Identity operation")

#used for: 判断是否两个变量是否是同一个对象的引用
a = 1
b = 2
print(a is b)

print('-------------------------------')
a = [1,2,3,4,5,6]
b = a
a.append(10)
print(a is b)
print("a{} b{}".format(a,b))

print('------------------------------')
a = [1,2,3,(1,2,3)]
b = a
a.remove(a[3])
print(a is b)

print('---------------deep copy---------------')
a = [1,2,3,(1,2,3)]
b = copy.deepcopy(a)
a.remove(a[3])
print("a{} b{}".format(a,b))
print()

print('---------------light copy---------------')
a = [1,2,3,[1,2,3]]
b = copy.copy(a)
a[3].remove(a[3][0])
a.remove(a[0])
print(a is b)
print("a{} b{}".format(a,b))
#会连着指针一起复制，就会导致深层次指向的空间被修改时，关联的变量也会出现问题