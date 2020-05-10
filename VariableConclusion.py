#六种类型 数字 字符串 列表 元组 集合 字典


#数字 不可变对象
a = 1
print(id(a))
b = a
a = 2
print(id(a))
print(a is b)
a += 10
a += 1.1
a *= 10
a /= 10
print(a)
a//=10
print(a)
a **= 2
print(a)

#字符串 增加 切片 查找
print('======================string operation========================')
a = "123aa ddqqe1"
b = "hello world"
c = a+b
print(c[::-1])
#print(c.index('0'))#index 找不到的时候会终止程序
print(c.find('0'))#找不到时会返回-1，以此标识字符有没有在字符串中

print(a[2])

print(a,b)

#列表 增删改查
print('======================list operation========================')
a = [1,2,3,4]
a.append(10)
a.extend([1,3,5])
a.append([1,2,3])
del a[2]
a.remove(a[len(a)-1])
print(a.index(1))
print(a)
print(a[::-2])
print(a)
print(sorted(a))
print(a)


#元组 增删改查 修改会创建一个新的元组
print('======================tuple operation========================')
a = (1,2,3,4)
print("before modify",id(a))
a = a[::-1]
print("after modify",id(a))

print(a.index(1))
print(a)

#集合 集合无序 不重复 只存放不可变类型 怎么查找? 集合的pop和字典的pop不一样
print('======================set operation========================')
a = set()#创建一个空集
a.add(5)
a.remove(5)
a.add('a')
b = [1,2,3,4,(1,2,3,4)]
print(set(b))
a = set(b)
a.pop()
print(a)

class type1:
    def __init__(self):
        self.own = (0)

b = type1()

#字典 增删 改 查 键值唯一，只能用不可变类型
print('======================dict operation========================')
a = {}#创建一个空字典
a[1] = 'hello,world'
a[0] = {1,2,3,4}
a[(1,2)] = [1,2,3,4]
del a[1]
a.pop(0)

print(a)
