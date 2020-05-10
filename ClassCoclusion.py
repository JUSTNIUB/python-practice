
#类和对象，属性，行为，继承，组合，构造函数和调用

#定义一个类
class myTestClass:
    def __init__(self,name,sex):
        self.name = name
        self.sex  = sex

    def show(self):
        print(f"name:{self.name} sex:{self.sex}")

class myTestClass2(myTestClass):
    def __init__(self,name,sex,hobby):
        self.name = name
        self.sex  = sex
        self.hobby = hobby
    def show1(self):
        print(f"name:{self.name} sex:{self.sex} hobby:{self.hobby}")

class myEye:
    def __init__(self,color):
        self.eyecolor = color

class myHair:
    def __init__(self,length):
        self.length = length
    def show(self):
        print("my hair is ",self.length)
class myColor:
    def __init__(self,color):
        self.color = color

class Person:
    def __init__(self,eye,hair,color):
        self.eye = eye
        self.hair = hair
        self.color = color

    def show(self):
        print(f"eye:{self.eye.eyecolor} hair:{self.hair.length} color:{self.color.color}")

    def __call__(self):
        print('hello,world')
a = myTestClass("华华",'女')
a.show()
b = myTestClass2("华华",'女','唱歌')
b.show1()

c = Person(myEye('black'),myHair('long hair'),myColor('yellow'))
c.hair.show()
c.show()
c()