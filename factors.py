num=int(input("enter a number:"))
fac=[]
for i in range(1,num+1):
    if num%i==0:
        fac.append(i)
print("factors:",fac)
