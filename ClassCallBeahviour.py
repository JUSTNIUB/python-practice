
#定义一个类，在类中重定义call行为，基于此类创建一个对象，并调用call
class person:
    def __call__(self):
        print("do not call me ,ok?")

li1 = person()
li1()