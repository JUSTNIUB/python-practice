
class Person:
    def __init__(self,name,height):
        self.name = name
        self.height = height

    def __add__(self,otherobject):
        return self.height+otherobject.height
    def __sub__(self,otherobj):
        return  self.height-otherobj.height

Hua = Person("Lily",158)
Jo  = Person("Johnson",162)

print(Hua+Jo)
print(Hua-Jo)
