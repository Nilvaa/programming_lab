f=open("letter.txt","r")
l=[i.split() for i in f]
print(l)
f.close()


