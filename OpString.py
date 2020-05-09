
#字符串操作 切片 查找 转义 拼接 格式化
a = "hello"
b = "world"

print(a+b)

print(a[1:])

print(a.index('h'))
print(a.find('o'))

print(a + '\n' +b)
#r 的作用 :抑制转义
print(r"hello\nworld")

print("{} {}".format(a,b))
print(f"{a},{b}")