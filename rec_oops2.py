class Rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return self.l*self.b
    def peri(self):
        return 2*(self.l+self.b)
l1,b1=map(int,input("enter length and breadth of rec 1:").split())
l2,b2=map(int,input("enter length and breadth of rec 2:").split())
r1=Rectangle(l1,b1)
r2=Rectangle(l2,b2)
area1=r1.area()
pe1=r1.peri()
area2=r2.area()
pe2=r2.peri()
if area1>area2:
    print("Area of the first rectangle is greater than second rectangle")
elif area2>area1:
    print("Area of the second rectangle is greater than first rectangle")
else:
    print("both are equal")
    

