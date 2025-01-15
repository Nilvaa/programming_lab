class Time:
    def __init__(self,h=0,m=0,s=0):
        self.h=h
        self.m=m
        self.s=s
    def __add__(self,other):
        se=self.s+other.s
        mi=self.m+other.m+se//60
        hr=self.h+other.h+mi//60
        return Time(hr%24,mi%60,se%60)
    def __str__(self):
        return f"{self.h:02}:{self.m:02}:{self.s:02}"
h1,m1,s1=map(int,input("enter hour1, minute1, second1:").split())
h2,m2,s2=map(int,input("enter hour1, minute1, second1:").split())
t1=Time(h1,m1,s1)
t2=Time(h2,m2,s2)
print("sum:",t1+t2)

