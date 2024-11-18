#Creating list data Structure
#using empty list:
l=[]
l.append(10)
l.append(20)
l.append("Rishabh")
print(l)

#dynamically using eval()
l1=eval(input("Enter some list items:"))
print(l1)
print(type(l1))

#using list()
s=input("Enter some alphanumeric characters:")
l2=list(s)
print(type(l2))
print(l2)

#using split()
s=input("Enter some String or alphanumeric characters:")
l3=s.split()
print(type(l3))
print(l3)

#Creating list if we know the list items already
l4=[10,20,30,40,50,'Rishabh']
print(l4)