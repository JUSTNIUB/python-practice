print('==========dict operation===========')

#建必须是唯一的，用于标识，可以是数字，字符串或者元组，字典也会有去重功能，即相同的键值
#只允许存在一个
a={'name':"zhang3","sex":'男',"age":36}
print(len(a))
print(a["name"])

class tu:
    pass

#增加
a["height"]=187
a[15]=60
a[(1,2,3)] = 100
print(a)

#删除
a.pop('height')

print(a)
#修改
a[(1,2,3)] = 112
print(a)



#查找