#Important methods of set

s={10,20,30,665,978,31}
s.add(66) #add() adds the item into the set
print("After add()",s)
l=[15,16,18,98,14]
s.update(l) #update() adds the sequence to the set
print("After update()",s)
s1=s.copy() #copy() creates the new clone object of the set
print("After copy()",s1)
print("After pop()",s1.pop()) #pop() removes the random element from the set
s1.remove(14) #remove() removes the particular element from the set if found otherwise returns key Error
print("After remove()",s1)
s1.discard(14) #discard() removes the particular element if found otherwise discard i.e do nothing
print("After discard()",s1)
s1.clear() #clear() remove all the element from the set and returns empty set
print("after clear()",s1)
