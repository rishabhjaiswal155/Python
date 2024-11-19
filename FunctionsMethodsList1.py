#Differrence between extend() and append() methods of list
l=[10,20,30,40,50]
l.extend('Rishabh') #extend() method append the item as a character by character to list
print(l)
l=[10,20,30,40,50]
l.append('Rishabh') #append() method appends the item as a whole string
print(l)

#remove()
n=int(input("Enter item to remove:"))
if n in l:  #condition checking is required to handle the ValueError
    l.remove(n)
    print("item",n,"removed successfully")
else:
    print("item",n,"is not present in list")

#pop() and pop(index)
print(l.pop())
print(l)
print(l.pop(3))
print(l)
