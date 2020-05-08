
#定义一个桌子类
class table:
    def shape(self,tbshape):
        print("it's a {} table".format(tbshape))


table1 = table()
table1.shape("round")

table2 = table()
table2.shape("square")