#组合：一个类可以由很多个类组成,即一个类中其中的一个属性就是 另外一个类

class Eye:
    def __init__(self,color):
        self.color = color

class High:
    def __init__(self,height):
        self.height = height

class Weigh:
    def __init__(self,weight):
        self.weight = weight

class Person:
    def __init__(self,eye):
        self.eye = eye          #这里的意思是定义类的一个属性为eye

    def initOtherAttributes(self,height,weight):
        self.High = height
        self.Weigh = weight

    def show(self):
        print(self.eye.color)
        print(self.Weigh.weight)
        print(self.High.height)


eye = Eye("black")
height = High(180)
weight = Weigh("65Kg")
p = Person(eye)
p.initOtherAttributes(height,weight)
p.show()