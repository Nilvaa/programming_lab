import csv
with open("stud.csv",mode="r")as file:
    print("details of column 2")
    csvr=csv.reader(file)
    for row in csvr:
        print(row[1],row[2])
    
