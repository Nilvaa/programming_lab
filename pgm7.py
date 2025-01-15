x=[int(i) for i in input("enter integers:").split()]
y=[int(i) for i in input("enter second list:").split()]
same=len(x)==len(y)
sum1=sum(x)==sum(y)
com=[i for i in x if i in y]
print(same)
print(sum1)
print(com)
