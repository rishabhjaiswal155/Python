#Accessing List elements using index,slice operator,Also List is mutable
l=[10,20,30,40,50,'Rishabh',[10,25,65]]
print(l[0],l[4],l[6][1])
print(l[::])
print(l[2:7:1])
l[0]=100
print(l)
