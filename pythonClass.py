#类的操作
#类型：静态属性，静态方法，类方法，对象方法，私有方法


class testclass():#不加括号有无关系？
    #类的成员属性
    var1 = 0

    def __init__(self,name):
        #对象的成员属性
        self.name = name

    @property#类不能直接调用静态属性，否则会报错，使用的时候可以不用加括号，当作属性一样使用
    def testStaticAttrFunc(x):
        print('aaa')
        return  10

    @classmethod#
    def testClassFunc(cls):
        print(cls.var1)

    @staticmethod
    def testStaticFunc():#一般不加参数，为了使类和对象都可以调用
        #不能直接调用类属性和对象属性，否则会报错
        #print(var1)
        print(testclass.var1)


tes = testclass('hello')
tes2 = testclass('jiujiu')
print(tes.testStaticAttrFunc)
tes.var1 = 20
tes2.var1 = 10
print(id(testclass.var1))
print(tes.var1 is tes2.var1)#类实例化后 类公共的静态属性不共用

testclass.var1 = 10
testclass.testStaticFunc()
testclass.testClassFunc()
#print(testclass.testStaticAttrFunc) #类不能调用静态属性

