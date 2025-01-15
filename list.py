'''l=input("enter number:")
li=[int(num) for num in l.split()]
p1=[num for num in li if num>0]
print("postive numbers:",p1)'''

'''l=input("enter numbers:")
l1=[int(num) for num in l.split()]
sq=[num*num for num in l1]
print("squares:",sq)'''

'''b=input("enter word:")
v=[char for char in b if char.lower() in"aeiou"]
print("voewls",v)'''

'''word=input("enter word")
val=[ord(char) for char in word]
print(val)'''

n=input("enter integers:")
num=n.split()
result=[]
for i in num:
    j=int(i)
    if j>100:
        result.append("over")
    else:
        result.append(j)
print(result)
