class Twovector:
    def __init__(self,i,j):
        self.i = i
        self.j = j
    def show(self):
        print(f"vector is {self.i}i + {self.j}j")
class threevector(Twovector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k
    def show(self):
        print(f"vector is {self.i}i + {self.j}j + {self.k}k")

m = Twovector(1,2)
n = threevector(6,2,3)
m.show()
n.show()
