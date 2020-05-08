#属性可以在外面进行修改，构造函数可以带参数，行为可以带返回值
class Person:
    def __init__(self,name):
        self.height = 100
        self.sex = "male"
        self.name = name
    def show(self):
        print("{}  {} {}".format(self.name,self.height,self.sex))


li1 = Person("Noname")
li1.show()
li1.height=123
li1.sex="female"
li1.show()


class Animal:
    def __init__(self,kind):
        self.kind = kind
        self.eat = "meat"
        self.size = "huge"
    def show(self):
        print(self.kind)
        print(self.eat)
        print(self.size)


rabbit = Animal("rabbit")
rabbit.eat = "grass"
rabbit.size = "small"
rabbit.show()

class Computer:
    def __init__(self,brand):
        self.brand = brand
        self.price = 10000
        self.perfomance = "great"
    def show(self):
        print("brand:",self.brand)
        print("price:",self.price)
        print("perfomance:",self.perfomance)

computer1 = Computer("Rox")
computer1.price=100
computer1.perfomance="poor"
computer1.show()





