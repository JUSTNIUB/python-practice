# a = 1 #定义一个变量 ;字符串和数字是不可变的
# b = 1.2#定义一个b变量，并赋值为浮点型1.2
c = "我爱中国" #定义一个c变量，并赋值为字符串
e = True #bool 型

class type1:
    def __init__(self):
        print("hello")

class person:
    def __init__(self,type1):
        self.type = type1



a = [1,2,3]
b = a
b.append(4)
d = person(a) #定义一个d 变量，类型为 person
print(a == b)

a = type1()
print("a=",a)
print("b=",b)
d.type = a
a = b
print("dtype = ",d.type)
print("e=",e)

print("-------------------------------")
