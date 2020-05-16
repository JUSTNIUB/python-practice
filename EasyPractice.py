import math
import random
#菜鸟驿站 python学习
print('----多行语句学习----')
#换行:在python中，如果一行写不下了，可以用\来换行。如果是列表，元组，字典等可以直接换行
total = 'item_one'+\
        'item_two'+\
        'item_three'
print(total)
total = ['item_one','item_two',
         'item_three','item_four']
print('多行语句',total)

#基本数据类型
print('----基本数据类型----')
counter = 100
miles = 10000
name = 'runoob'
print(counter,miles,name)
name = 100
print('id',id(counter),id(miles),id(name)) #使用id查看对象所在的地址空间 这里的地址空间应该是虚地址，不是实地址
#多变量赋值, 在python里，可以把=也看作是一种对象
print('----多变量赋值----')
a = b = c = 1                             #多目标赋值，= 可以看成是一个函数。比如序列赋值，比如等等,如果有不定长参数，则会组合成列表，而非元组(注意)
print(a,b,c)
a,b,c = 1,2,'hello'
print('序列赋值',a,b,c)
#*a,b,*c = 1,2,3,4,5,6,7 这种写法错误，不能出现两个未知大小的数
a,*b,c = 1,2,3,4,5,6,7
a,b,*c = 1,2,3,4,5,6,7
*a,b,c = 1,2,3,4,5,6,7
print('序列 队列 赋值',a,b,c)

#数字  type查询变量所指的对象类型 字典可以像列表一样通过键访问值
a,b,c,d = 1,5.0,True,type(a)
print(a,b,c,d)
dict1 = {'s':'ssad'}
del dict1['s']
print(dict1)

#数值运算
print('----数值运算----')
print(5+4)
print(4.3-2)
print(3*7)
print(2/4)
print(2//4)
print(17%3)
print(2**5)
print(4.53e-1J)

#字符串
print('----字符串----')
mystr = 'runoob'
print(mystr)
print(mystr[0:-1])
print(mystr[0])
print(mystr[2:5])
print(mystr[::-1])
print(mystr[:0:-1])
print(mystr*2)
print(mystr+'TEST')
print('ru\noob')
print(r'roo\nob')

#列表
print('----list----')
mylist =[1,2,3,4,'s','s',2,1]
print(mylist)
print(mylist[0])
print(mylist[1:3])
print(mylist[2:])
print(mylist*2)
print(mylist+[1,2,3])

#运算符
print('----------operator----------')
a=10
b=21
c=0
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
a=5
b=3
print(a**b)
print(a//b)

a = 21
b = 10
c = 0
if a==b:
    print('等号 ：a 和 b相等')
else:
    print('等号 ：不相等')

if a!=b:
    print('不等号 ：a和b不相等')
else:
    print('不等号 ： ab相等')

if(a<b):
    print('小于号: a 小于 b')
else:
    print('小于号：a 大于 b')

if(a>b):
    print('大于号: a大于b')
else:
    print('大于号: a小于b')

a = 21
b = 10
c = 0
c = a+b
c += a
print('+',c)
c *= a
print('*',c)
c /= a
print('/',c) # 除号变成了浮点数
c = 2
print('=',c)
c %= a
print('%',c)
c **= a
print('**',c)
c //= a
print('//',c)
print(a is b)

#number,在整数除法中，除法总是会返回一个浮点数
var1 = 10
var2 = 20
print(var1,var2)
print(var2/var1)
print(var2//var1)
var1 = 2.0
print(var2//var1)
print(math.pi)
print(round(math.pi,3))
print(random.randrange(0,10,1))

#string
print('---------string------------')
var1 = 'hello,world'
var2 = 'Runoob'
print('var1[0]',var1[0])
print('var2[1:5]',var2[1:5])
print(var1[5:]+'nonono')
print('---===---=====')
print('---------\\--')
print('---------\'--')
print('---------\"--')
print('---------\a--')
print('---------\b--')
print('---------\000--')
print('---------\n--')
print('---------\v--')
print(r'---------\\--')
print('n' not in '---------\a--')
a = 'hello'
b = 'python'
print('a+b',a+b)
print('a*2',a*2)
print('a[1]=',a[1])
print('a[1:4]:',a[1:4])

if('H' in a):
    print('H 在变量 a中')
else:
    print("H 在变量a中")
print(f"{'你好'}，{'thank u'}")            #字符串操作的一些方法，用到时再去查
print("{}，{}".format('你好','yes,hello'))
print('llelalaq'.capitalize())
print('llelalaq'.count('ll'))
print('ssasd'.find('z'))                 #字符串 查找find index,区别在于如果找不到index 会返回一个错误
print('ssasd'.index('s'))
print(' ssasd'.lstrip())

#list operation 增删改查 append extend  remove del pop find index 索引为参数的支持负索引，支持切片
print('========list========')
list1 = ['google','runoob',1966,2000]
list2 = [1,2,3,4,5,6]
list3 = [i for i in range(10,0,-1)]
print(list1)
print(list2)
print(list3)
print(list1[1])
list2 = list2[2::2]
print(list2)
list2.append(3)
print('add 3:',list2)

del list3[2]
print(list3)
print(len([1,2,3]))
print([1,2,3]+[4,5,6])
list4 = [1,2,3,3,4]
print("{}, lenth:{},max:{},min:{}".format(list4,len(list4),max(list4),min(list4)))
list4.pop(-1) #index
print(list4)
list4.remove(1)#element
print(list4)

print(list4.count(3))
a = list4.copy()
list1 = list4
print(a is list4,list1 is list4)

#tuple
print('\n--------tuple-------\n') #支持切片操作，序列操作 + *  index没有find in 属于可迭代对象
tup1 = ('hello',1,2,3)
print(tup1)
tup2 = (1,2,3,4,5)
print(type(tup2))
print(tup2.index(1))

print(tup2[::-1])
del tup2#删除对象

#print(tup2)
print(1 in tup1)
print(len(tup1))
print(tup1+(1,3,4))
print(tup1*2)
tup2 = tuple([i for i in range(10)])
print(tup2)
tup2 = ('1,1','2','8')
print(tup2)
print(max(tup2))
print(min(tup2))

#字典 键为不可变对象 增删改查  数组操作增加 pop del，带键 数组操作修改  in 查找(只能查建 貌似)
print('\n====================================\n')
print('\n---------dictionary---------\n')
dict1 = {'s':1,'a':2}
print(dict1)
print(dict1['s'])
del dict1['s']
print(dict1)
dict1['d'] = 15
print(dict1)

dict2 = {1:2,1:3,1:'a',2:3}
print(dict2)
print(len(dict2))
print(str(dict2))
print(1 in dict2)
a = '123456'
print('12' in a )
dict2.pop(1)
print(dict2)

#集合 元素为不可变对象 使用set函数和update 方式时，实际上是将对象作为迭代器使用，取其中对应坐标的参数 set()函数的操作比较有趣
print('-------------set operation-------------')
set1 = set()#创建一个空集
print(type(set1))
basket = {'apple','orange','apple','pear','orange','banana'}
print(basket)
print('apple' in basket)

a = set('adsasdsadasdasdqwe')#把字符串分割了,应该是类似一个迭代器
b = set('1swzxgasydsf1234')
#print(str(a))
a = set('1234567')
print(a-b)              #增加 add()添加单个元素 update()比较好用，可以添加很多个
print(a|b)              #集合间的操作，并 交 差 (并集-差集)
print(a & b)            #删除： discard pop remove
print(a ^ b)            #查找： in
                        #
a = {i for i in 'llqqooaasjx'}
print(a)
a = {1,2,3,"asd"}
print(a)
a.add(5)
print('change',a)
a.update([1,2,3,10]) #调用了迭代器
print(a)
a.update({7:'sss',3:4})#只加入了字典中的健
print(a)
a.update('sss11sdfkhjai')
print(a)
a.update((5,1,3,'ppp'))
print(a)
a.update({521, 1, 3, 'pppt'})
print(a)

a.remove(521)
print(a)
a.discard(10)#这里好像字符串和数字是一样的？ 但是数字只能用数字删除
print(a)
a.pop()#随机删除
print(a)
print(len(a))
a.clear()
print(a)
print(1 in a)

#斐波那契数列
a,b = 0,1
while b<1000:
    print(b,end=' ')
    a,b = b,a+b

#函数: 如果用列表或者字典当作不定长参数，调用时要在前面加**  另外没有return的函数返回的是None
print('\n-----fucntion--------\n')
def helloFunc():
    print('\nhello,myfirst function')
helloFunc()

def area(width,height):
    return width*height
print(area(10,20))

def ChangeInt(a):
    a = 10

b = 2
ChangeInt(b)
print(b)

def changeme(mylist):
    mylist.append([1,2,3,4])
    print(mylist)

mylist = [10,20,30]
changeme(mylist)
print(mylist)

def printme(str):
    print(str)
    return
printme(str="hello,liewei")

def printinfo(name,age=35):
    print(f"名字{name},年龄{age}")
    return
printinfo(name='hello')
def printinfo1(arg1=0,*vartuple):
    print('输出')
    print(arg1)
    print(vartuple)
    return
printinfo1()
printinfo1(1,2,3,4,5,6)
def printinfo2(arg1,**vardict):
    print(f"{arg1},{vardict}")
    return
printinfo2(1,b=3)

a = [1,2,3,4,5]
printinfo1(*a)
b = {'1':2,'3':4,'5':6}
printinfo2(10,**b)

b = lambda x,y:x+y
print(b(1,2))

#数据结构
a = [66.25,333,333,1,1234.5]
print(a.count(333),a.count(66.25),a.count('x'))
a.insert(2,-1)
a.append(333)
print(a)
print(a.index(333))
a.remove(333)
print(a)
a.reverse()
print(a)
a.sort()
print(a)
a.pop()
print(a)

#列表推导式
print('----------list -----------')
vec = [2,4,6]
vec2 = [3,4,5]
print([3*x for x in vec])
print([[x,x**2] for x in vec])
print([[x for x in range(n-2,n)] for n in range(10)if n>2 and n%2==0])
print([x*y for x in vec for y in vec2])
print([str(round(355/133,i)) for i in range(1,6)])

#矩阵 :
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]
#内循环：访问所有的子列表，取出其中第n个元素，即把同一列的元素都取出来,有多少行就有多少次循环。 外循环，共有几列
#
print([[row[i] for row in matrix] for i in range(len(matrix[0]))])
a = [0,1,2,3,4,5,6]
del a[2:4]
print(a)

#元组和序列 =号也是一个对象，不定长参数会以元组的方式传进去，
print('\n======tuple struct======\n')
t = 12345,54321,'hello',12345
u = t,1,2,3
print(t)
print(u)

#字典,字典的常用赋值方法 字典推导式
a = dict([('space',4133),('guido',4127),('jack',4098)])
a = {x:[i for i in matrix[x]] for x in range(len(matrix))}
print(a)
#字典遍历
for k,v in a.items():
    print(k,v)

#序列遍历
for i,v in enumerate(['tic','tac','toe']):
    print(i,v)

questions = ['name','queit','favorite color']
answers   = ['lancelot','the holy grail','blue']
for q,a in zip(questions,answers):
    print('what is your {0}? It is {1}.'.format(q,a))

#反向遍历
for i in reversed(range(1,10,2)):
    print(i)
#顺序遍历
basket = ['apple','orange','apple','pear','orange','banana']
for f in sorted(set(basket)):
    print(f)
j = [1,2,3,4]
i = [4,3,2,1]
print([[x,y] for x,y in zip([c for c in range(10)],[d for d in range(10,0,-1)])])


#import 语句 包就是普通文件夹中放了一个__init__.py文件
import fibo
fibo.fib(1000)
# from fibo import fib as fibfunc
# fibfunc(10)
print(dir())
import testpack.tpackhello as test
test.func1()

#输入和输出
print('----------python in and out-----------')
s = 'Hello,Runoob'
print(str(s))
print(repr(s))
print(str(1/7))
print(repr(10*3.25),repr(40000))
print(repr('hello,runoob\n'))
print(repr((1,2,3,[5,1,2,3])))

for x in range(1,11):
    print(repr(x).rjust(2),repr(x*x).rjust(3),repr(x*x*x).rjust(4))

for x in range(1,11):
    print('{0:2d} {1:3d} {2:4d}'.format(x,x*x,x*x*x))

print('12'.zfill(5))
print('{} 网址："{}!"'.format('github','www.github.com'))
print('{name} 网址："{site}!"'.format(site='github',name='www.github.com'))
print('{!a}'.format(ascii('a')))
print('常量PI的值为{0:.3f}'.format(math.pi))
print('常量PI的值为{:.3f}'.format(math.pi))# 这样写就是错的
table = {'google':1,"tabao":2,"liewei":3}
for x,y in table.items():
    print("{:10} ==> {:10d}".format(x,y))
print('Google:{0[google]:d}; taobao:{0[tabao]:d}'.format(table))

#类的定义
print('\n===========Class==============\n')
class MyClass:
    i = 12345
    def f(self):
        return 'hello,world'

x = MyClass()
print("Myclass 类的属性i为:",x.i)
print("MyClass 类的方法 f 输出为：",x.f())

class Complex:
    def __init__(self,realpart,imagpart):
        self.r =realpart
        self.i = imagpart

x = Complex(3,4)
print(x.r,x.i)

#这里的self 指的是对象的self，而非类
class Test:
    def prt(self):
        print(self)
        print(self.__class__)

t = Test()
t.prt()

class people:
    def __init__(self,n,a,w):
        self.name = n
        self.age  = a
        self.__weight = w
    def speak(self):
        print('{} say: I am {} years old'.format(self.name,self.age))

p = people('Johnson',26,111)
p.speak()

#继承 父类调用可以用父类名
class student(people):
    grade = ''
    def __init__(self,n,a,w,g):
        people.__init__(self,n,a,w)
        self.grade = g
    def speak(self):
        print(f"{self.name} say: I am {self.age} years old,and on {self.grade} grade now ")

s = student('ken',10,60,3)
s.speak()

class speaker:
    def __init__(self,n,t):
        self.name = n
        self.topic = t
    def speak(self):
        print(f"Myname is {self.name}.The topic of my speech is {self.topic}")
        return
class sample(speaker,student):
    def __init__(self,n,a,w,g,t):
        student.__init__(self,n,a,w,g)
        speaker.__init__(self,n,t)

test = sample('Johnson',25,80,4,"Chip")
test.speak()

class Vector:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        return
    def __str__(self):
        return 'Vector (%d,%d)'%(self.a,self.b)
    def __add__(self,other):
        return Vector(self.a+other.a,self.b+other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)
print(v1+v2)