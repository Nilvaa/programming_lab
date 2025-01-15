s=input("enter a string:")
if s:
    f=s[0]
    m=f+s[1:].replace(f,'$')
    print(m)
