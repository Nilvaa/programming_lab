s,f=map(int,input("enter starting and ending years:").split())
for i in range(s,f+1):
    if i%400==0 or 1%100!=0 and i%4==0:
        print(i)
