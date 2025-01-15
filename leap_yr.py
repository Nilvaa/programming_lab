c=int(input("enter starting yr:"))
f=int(input("enter final yr:"))
for i in range(c,f+1):
    if i%400==0 or i%100!=0 and i%4==0:
        print(i,"is a leap year")
