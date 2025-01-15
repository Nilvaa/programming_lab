'''import math

n,m=map(int,input("enter 2 numbers:").split())
print(math.gcd(n,m))'''

'''fruit={16:"orange",26:"apple",3:"mango"}
veg={1:"carrot",2:"beans",3:"chilly"}
d=dict(sorted(fruit.items()))
d2=dict(sorted(fruit.items(),reverse=True))
print(d)
print(d2)'''

s=input("enter string:")
if s:
    fc=s[0]
    m=fc+s[1:].replace(fc,"$")
else:
    m=""
print(m)
