class Bank:
    def __init__(self,ac_no,ac_na,ty,bal):
        self.ac_no=ac_no
        self.ac_na=ac_na
        self.ty=ty
        self.bal=bal
    def deposit(self,amt):
        if amt>0:
            self.bal+=amt
            print("deposited:",self.bal)
        else:
            print("invalid amount")
    def withdrw(self,amt):
        if amt>self.bal:
            print("insuffiecent balance")
        else:
            self.bal-=amt
            print("withdrawed:",amt," Current balance",self.bal)
    def details(self):
        print("account")
        print("account number:",self.ac_no)
        print("account name:",self.ac_na)
        print("account type:",self.ty)
        print("balance:",self.bal)
no=int(input("enter account number:"))
nam=input("enter name:")
ty=input("enter account type:")
ba=int(input("enter balance:"))
b1=Bank(no,nam,ty,ba)
while True:
    print("1.deposit")
    print("2.withdraw")
    print("3.current balance")
    print("4) View Details")
    print("5) Exit")
    ch=int(input("enter choice:"))
    if ch==1:
        amt=int(input("enter amount:"))
        b1.deposit(amt)
    elif ch==2:
        amt=int(input("enter amount:"))
        b1.withdrw(amt)
    elif ch==3:
        print("current balance:",b1.bal)
    elif ch==4:
        b1.details()
    elif ch==5:
        break
