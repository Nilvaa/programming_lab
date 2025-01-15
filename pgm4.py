li=input("enter a line of text:")
wrds=li.split()
co={}
for i in wrds:
    i=i.strip('.,!?";:')
    if i in co:
        co[i]+=1
    else:
        co[i]=1
print(co)
