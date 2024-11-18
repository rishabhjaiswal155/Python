#Manipulating elements in the list
l=[]
l.append(10) #append() is used to insert the element in list at last
l.append(20)
l.append('Rishabh')
print(l)
l.insert(0,58) #insert() is used to insert the element in list at particular index
print(l)
l.insert(50,100)
l.insert(-11,999)
print(l)

l=['Rishabh','Vishal','Amol'] #extend() is used to extend the one list with other
l1=['IACSD','PharmaAce','Pragati']
l.extend(l1)
print(l)
print(l1)