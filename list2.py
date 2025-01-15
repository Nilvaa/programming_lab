'''n=int(input("enter number:"))
fa=[]
for i in range(0,n):
    if n%i==0:
        fa.append(i)
print("factors:",fa)'''

'''w=input("enter words:").split()
l=max(w,key=len)
print(len(l))'''

'''s=input("enter string:")
if len(s)>=3:
   if s.endswith("ing"):
       r=s+"ily"
   else:
       r=s+"ing"
else:
    r=s;
print(r)'''
'''n=int(input("enter number:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i*j,end=' ')
    print()'''
'''l=[int(i) for i in input("enter list:").split()]
print(sum(l))'''
'''n=int(input("enter number:"))
f=1
for i in range(n,1,-1):
    f=f*i
print(f)'''
l=[int(i) for i in input("enter number:").split()]
l2=[i for i in l if i%2!=0]
print(l2)
