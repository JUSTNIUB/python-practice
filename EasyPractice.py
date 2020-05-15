import math
import random
#菜鸟驿站 python学习
print('----多行语句学习----')
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
print('id',id(counter),id(miles),id(name))
#多变量赋值, 在python里，可以把=也看作是一种对象
print('----多变量赋值----')
a = b = c = 1
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
print(f"{'你好'}，{'thank u'}")
print("{}，{}".format('你好','yes,hello'))
print('llelalaq'.capitalize())
print('llelalaq'.count('ll'))
print('ssasd'.find('z'))
print('ssasd'.index('s'))
print(' ssasd'.lstrip())

#list operation
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
print('--------tuple-------')
tup1 = ('hello',1,2,3)
print(tup1)
tup2 = (1,2,3,4,5)
print(type(tup2))

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

#字典 键为不可变对象
print('====================================')
print('---------dictionary---------')
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

#集合 元素为不可变对象 使用set函数和update 方式时，实际上是将对象作为迭代器使用，取其中对应坐标的参数
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
print(a-b)
print(a|b)
print(a & b)
print(a ^ b)
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

#函数
print('-----fucntion--------')
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
print([[row[i] for row in matrix] for i in range(len(matrix[0]))])

a = [0,1,2,3,4,5,6]
del a[2:4]
print(a)

#元组和序列 =号也是一个对象，不定长参数会以元组的方式传进去
t = 12345,54321,'hello'
u = t,1,2,3
print(t)
print(u)

#字典,字典的常用赋值方法
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
