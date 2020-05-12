#函数进阶


def testArg(a):
    print('insight')
    print(id(a))
    a = 10
    print(id(a))


#传参：可变对象与不可变对象
b = 2
print(id(b))
testArg(b)
print(b)

print('=====================function arg=====================')
#函数参数
def testArg1(reqArgs):
    print(reqArgs)
    return
testArg1('hello,req')
#关键字参数
def testArg2(reqArgs,keyArgs):
    print(reqArgs,keyArgs)
    return
testArg2(keyArgs='hello',reqArgs='hello')
#默认参数 默认参数要放在必须参数后面
def testArg3(keyArgs,reqArgs='hello'):
    print('-------reserved argument-------')
    print(keyArgs,reqArgs)
    return

testArg3('nono')
def testArg4(keyArgs,regArgs = '')