import csv
d=[{"name":"carrot","price":"28","color":"orange"},{"name":"beans","price":"33","color":"green"},{"name":"beetroot","price":"32","color":"magenta"},{"name":"lemon","price":"12","color":"yellow"},{"name":"radish","price":"22","color":"white"}]
field=['name','price','color']
filename=['veg.csv']
with open('veg.csv','w',newline='')as file:
    w=csv.DictWriter(file,fieldnames=field)
    w.writeheader()
    w.writerows(d)
with open("veg.csv",mode="r")as file:
    c=csv.reader(file)
    for i in c:
        print(i)
