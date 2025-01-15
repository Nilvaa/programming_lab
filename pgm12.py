file=input("enter file name:")
dot=file.rfind('.')
if dot!=-1 and dot!=len(file)-1:
    ex=file[dot+1:]
    print(ex)

