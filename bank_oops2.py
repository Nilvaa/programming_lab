class Account:
    def __init__(self,acc_no,acc_na,acc_ty,bal):
        self.acc_no=acc_no
        self.acc_na=acc_na
        self.acc_ty=acc_ty
        self.bal=bal
    def dep(self,amt):
        if amt>0:
            self.bal+=amt
            print("successfully deposited",self.bal)
        else:
            print("invalid amount")
    def withd(self,amt):
        if amt>self.bal:
            print("insufficent balance")
        else:
            self.bal-=amt
            print("withdrawed:",self.bal)
    def details(self):
        print("ACCOUNT DETAILS")
        print("_______________")
        print("Account Name:",self.acc_na)
        print("Account Number:",self.acc_no)
        print("Account type:",self.acc_ty)
        print("Account Balance:",self.bal)
ano=int(input("enter account number:"))
ana=input("enter account name:")
ty=input("enter account type:")
bal=int(input("enter balance:"))
b=Account(ano,ana,ty,bal)
while True:
    print("Menu")
    print("1)Deposit")
    print("2)withdraw")
    print("3)Current balance")
    print("4)View details")
    print("5)Exit")
    ch=int(input("enter choice:"))
    if ch==1:
        amt=int(input("enter amount to deposit:"))
        b.dep(amt)
    elif ch==2:
        amt=int(input("enter amount to withdraw:"))
        b.withd(amt)
    elif ch==3:
        print("current balance:",b.bal)
    elif ch==4:
        b.details()
    elif ch==5:
        print("Exited")
        break
    else:
        print("Invalid")
        


    

    
