class Publisher:
    def __init__(self,name):
        self.name=name
    def display(self):
        pass
class Book(Publisher):
    def __init__(self,name,tit,auth):
        super().__init__(name)
        self.tit=tit
        self.auth=auth
    def display(self):
        pass
class Python(Book):
    def __init__(self,name,tit,auth,pri,pgs):
        super().__init__(name,tit,auth)
        self.pri=pri
        self.pgs=pgs
    def display(self):
        print("Book Details")
        print("Publisher:",self.name)
        print("title:",self.tit)
        print("author:",self.auth)
        print("price:",self.pri)
        print("pages:",self.pgs)
na=input("enter publisher name:")
ti=input("enter Title:")
au=input("enter author name:")
pr=int(input("enter price:"))
pg=int(input("enter pages:"))
b=Python(na,ti,au,pr,pg)
b.display()
        
