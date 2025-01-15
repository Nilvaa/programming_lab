l1=[int(i) for i in input("enter integers:").split()]
p1=[i for i in l1 if i>0]
print(p1)

l1=[int(i) for i in input("enter numbers:").split()]
sq=[i*i for i in l1]
print(sq)

b=input("enter word:")
v=[c for c in b if c.lower() in "aeiou"]
print(v)

w=input("enter a word:")
o=[ord(v) for v in w]
print(o)
