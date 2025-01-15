import csv
'''d=[{"name":"vivan","Age":"22","course":"MCA"},
   {"name":"erica","Age":"25","course":"MBA"},
   {"name":"giva","Age":"22","course":"MBBS"},
   {"name":"kartik","Age":"20","course":"Bcom"}]
field=['name','Age','course']
filename=['stud2.csv']
with open('stud2.csv','w') as file:
    w=csv.DictWriter(file,fieldnames=field)
    w.writeheader()
    w.writerows(d)'''
with open('stud2.csv',mode="r")as file:
    c=csv.reader(file)
    for row in c:
        print(row)
