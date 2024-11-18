#Functions and Methods of List
l=[10,20,30,40,10,'Rishabh',25]
print(len(l)) #len() is Function
print(l.count(10)) #count() is method

#index() method using memebership index
l=[10,20,30,40,50,'Rishabh']
x=eval(input("Enter item to search the index:"))
if x in l: #Condition checking with if and membership in to avoid valueError
    print(l.index(x)) #index() is method
else:
    print("Item:",x,"is not present")