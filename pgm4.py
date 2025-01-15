s,e=map(int,input("enter starting and ending digits:").split())
res=[]
for i in range(int(s**0.5),int(e**0.5)+1):
    sq=i*i
    di=str(sq)
    if all(int(d)%2==0 for d in di):
        res.append(sq)
print(res)
