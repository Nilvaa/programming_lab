l1=[i for i in input("enter color list1:").split()]
l2=[i for i in input("enter color list2:").split()]
res=[i for i in l1 if i not in l2]
print(res)
