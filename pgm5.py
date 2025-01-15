s=input("enter list of integers:")
num=s.split()
re=[]
for n in num:
    i=int(n)
    if i>100:
        re.append("over")
    else:
        re.append(i)
print(re)
