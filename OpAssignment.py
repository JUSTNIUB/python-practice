#assignment operator : + - * / // **

#+ 可以用于数字，序列间的拼接，如果类中重构了+也可以使用
a = 3
b = 5
print(a+b)
print('a'+'basdasd')
print([123,4]+[213,'asd']+['1'])
a = ('asd',1,2)
b =  ('asd',3,4,5,6)
a += b
print(a+b)
print({'a':1234,1:1,5:123,1:123})

#- 两个数相减，也可以进行重载
a = 3
b = 5
print(a-b)

#* 两个数相乘，或者序列操作，乘多次,或者类中重载了运算符
a = 3
b = 5
print(a*b*10)
print("123"*3)
print([1,2,3]*3)
print((1,23,4)*4)
#print({12,3})

#** 幂运算 数字运算
print(a**5)

#//整除，不带小数点的
print(a/b)
print(a//b)

#% 取余运算
print(a%b)