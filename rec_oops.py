class Rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return self.l*self.b
    def peri(self):
        return 2*(self.l+self.b)
l1,b1=map(int,input("Enter l and b for 1st:").split())
l2,b2=map(int,input("Enter l and b for 2st:").split())
r1=Rectangle(l1,b1)
r2=Rectangle(l2,b2)
a1=r1.area()
a2=r2.area()
p1=r1.peri()
p2=r2.peri()
print("area 1:",a1)
print("area 2:",a2)
print("perimeter 1:",p1)
print("perimeter 2:",p2)
if a1>a2:
    print("area 1 is greater")
elif a2>a1:
    print("area 2 is greater")
else:
    print("area 1 = area2")

