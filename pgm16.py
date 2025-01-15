st1=input("enter the first:")
st2=input("enter the second:")
if len(st1)>1 and len(st2)>1:
    nst1=st1[0]+st2[1]+st1[2:]
    nst2=st2[0]+st2[1]+st2[2:]
    re=nst1+" "+nst2
    print(re)

