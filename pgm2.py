n=int(input("enter a number:"))
f=0
s=1
print(f)
print(s)
for i in range(0,n-2):
    t=f+s
    print(t)
    f=s
    s=t
