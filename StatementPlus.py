

#列表推导式

a_list = [1,2,3,4,5,6]
b_list = []

for a in a_list:
    b_list.append(a*2)
print(b_list)


#使用列表推导式创造一个矩阵
c_list = [[x for x in range(y-3,y)] for y in range(22) if y%3==0 and y!=0]
print(c_list)