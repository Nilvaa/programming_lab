area_sq=lambda s:s*s
area_tri=lambda b,h:0.5*b*h
area_rec=lambda l,w:l*w
s=int(input("enter side of square:"))
b,h=map(int,input("enter base and height:").split())
l,w=map(int,input("enter length and width:").split())
print("area of square:",area_sq(s))
print("area of triangle:",area_tri(b,h))
print("area of rectangle:",area_rec(l,w))
