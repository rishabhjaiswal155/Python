#Comparing two List Object using ==,>,>=,<,<=
l1=[10,20,30,40,50,'Rishabh']
l2=[10,20,40,50,30,'Rishabh']
l3=[10,20,30,40,50,'Rishabh']
print(l1==l2) #False
print(l1==l3) #True

''' Two List Objects are equal,if:
1.The contents in both list are same(including case).
2.The Order of Elements in both list are same.
3.The number of elements in both list are same.'''

print(l1)
l1.clear() #clear() function remove all the elements in the List
print(l1)

