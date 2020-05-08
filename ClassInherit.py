# 继承:父类子类之分，子类具有父类的全部属性和行为，但同时会拥有自己独特的属性和行为.
# what's attribute and behaviour
# 在子类中通过super().  来调用父类的成员函数，如果有多个父类，可以直接调用任意父类的属性和行为
# 在子类中可以重新定义属性和行为，子类的对象在执行行为时使用的就是重定义后的行为

class Animal:
    def __init__(self,name):
        self.name = name

    def show(self):
        print(self.name)

class Cat(Animal):

    def __init__(self,name):
        super().__init__(name)
        #print(self.name)
        self.name=  "cat"
        self.eat = "fish"
    def show(self):
        print(self.eat)

cat2 = Animal("cat")
cat2.show()

cat1 = Cat("meow")
cat1.show()



