st=input("enter a string:")
fr={}
for c in st:
    if c in fr:
        fr[c]+=1
    else:
        fr[c]=1
for c,count in fr.items():
    print(c,":",count)
