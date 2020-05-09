#循环控制语句

#类似于切片 range是一个迭代器
for i in range(-1,10):
    print(i,end='')


print('\n==========================')
#遍历列表 这里有点像是序列赋值，迭代器取出一个元素后赋值给前面的变量
for i,j in [[1,2]]:
    print(i,j,end=' ')


print('\n==========================')
#带索引的遍历
for i,a in enumerate(reversed(range(0,10)),0):
    print(f"{i}:{a}",end=' ')

print('\n==========================')
#遍历dict
mydict = {"name":"zhang","sex":"female"}
for key,value in mydict.items():
    print(f"{key}:{value}",end=' ')

#break and countinue command
for i in range(10):
    if i == 5:
        continue
    if i == 9:
        pass
        #break
    print(f"number:{i}",end=' ')

