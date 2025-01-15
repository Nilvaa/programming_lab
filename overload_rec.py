class Rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return self.l*self.b
    def __lt__(self,other):
        return self.area()<other.area()
l1,b1=map(int,input("enter length and breadth of rec 1:").split())
l2,b2=map(int,input("enter length and breadth of rec2:").split())
r1=Rectangle(l1,b1)
r2=Rectangle(l2,b2)
if r1<r2:
    print("area of rec 1 is smaller")
elif r2<r1:
    print("area of rec 2 is smaller")
else:
    print("both area are same")
