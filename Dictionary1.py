#Updating the dictionary

d={100:'Rishabh',200:'Amol',300:'shreyash'}
d[100]='Vishal' #if key is present then it will perform update,if not present it will perform add
print("After updating:",d)

#delete the elements from dictionary using del
k=int(input("Enter the key to delete the element:"))
if k in d:
	del d[k]
	print("deletion successfull")
else:
	print("Key",k,"is not present to delete the item")

#delete all the elements in dictionary
print(d)
d.clear()
print("After clear():",d)

#Difference between clear() and del
d1={100:'Rishabh',200:'Amol',300:'Shreyash'}
d2={101:'Lucky',102:'surabhi',103:'Priyanka'}
d1.clear() #clear() will only deletes the item from dict,not deletes the whole dictionary,it returns {} empty dict
print("AFter clear():",d1)
d1[102]='Mansi'
print(d1)

del d2 #del will delete the reference variable and marked the corresponding object for Garbage collection
#d2[106]='Chris' #It gives error is d2 is not defined
#print(d2) #It gives error is d2 is not defined

#specifying multivalues in the dictionary
d={100:'Rishabh',101:'Vishal',102:'Amol',103:'Shreyash'}
d[104]=['Mansi','Lucky']
print("specifying mutiple values:",d)

l=['Marathi','Gujrati','Hindi']
d={100:l}
print("specifying mutiple values:",d)