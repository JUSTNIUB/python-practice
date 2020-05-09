

#set 的类型转换
a = [i for i in range(10)]

a.extend(a)

print(a)

print(list(set(a)))