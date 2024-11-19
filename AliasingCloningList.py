#Aliasing and Cloning the List
x=[10,20,30,40,50,60,'Rishabh']
y=x #It is aliasing the list i.e List object is shared among two reference
print(id(x),id(y))

x1=[10,20,30,40,50,60,'Jaiswal']
x2=x1[:] #It is called as cloning using slice operator i.e new List object is created
print(id(x1),id(x2))

y1=[10,20,30,40,50,60,7,0]
y2=y1.copy() #It is cloning using copy() i.e new List Object is created
print(id(y1),id(y2))

