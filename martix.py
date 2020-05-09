
#实现两个矩阵的加法

class martix1:
    def __init__(self,myrow,myrank):
        self.row = myrow
        self.rank = myrank
        self.data = [[i for i in range(j-self.rank,j)] for j in range(self.row*self.rank+self.rank) if j%self.rank==0 and j!=0]

    def __add__(self,othermartix):
        if (self.row == othermartix.row) and (self.rank==othermartix.rank):
            newmartix = [[self.data[y][x]+othermartix.data[y][x] for x in range(self.rank)] for y in range(self.row)]
            return newmartix
        else:
            print("martix is not match")


a = martix1(5,2)
b = martix1(5,2)
print(a.data)
print(b.data)
print(a+b)
