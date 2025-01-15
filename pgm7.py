st=input("enter a string:")
if len(st)>=3:
    if st.endswith("ing"):
        res=st+"ly"
    else:
        res=st+"ing"
else:
    res=st
print("modified:",res)
