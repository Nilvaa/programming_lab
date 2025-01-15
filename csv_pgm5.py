import csv
d=[{"name":"canny","breed":"beagle","age":"2"},{"name":"snoopy","breed":"pug","age":"7"},{"name":"cookie","breed":"pomerianian","age":"5"},{"name":"bella","breed":"retriever","age":"2"}]
field=['name','breed','age']
filename=['dogs.csv']
with open('dogs.csv','w',newline='')as file:
    w=csv.DictWriter(file,fieldnames=field)
    w.writeheader()
    w.writerows(d)
with open("dogs.csv",mode="r")as file:
    c=csv.reader(file)
    for i in c:
        print(i)
