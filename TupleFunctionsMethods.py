#Important fnctions of tuple

t=(10,20,30,40,'Rishabh')
print(len(t)) #len() function of tuple

t=(10,1,32,20,10,20,78,10)
print(t.count(10))     #count() method of tuple
x=int(input("Enter number to find its index:"))
if x in t:
	print("index of item:",x,"is:",t.index(x))	#index(item) returns the index of first occurence of item
else:
	print("item",x,"not present in t",t)

t=(10,20,598,25,14,65,87)
l=sorted(t) #sorted() sorts the tuple object in natural order i.e Ascending
print(type(l),l) #sorted() return the list object
print(tuple(l))

t=('Rishabh','Raj','Abhilasha','durga','Rashmika','sharvari')
t1=tuple(sorted(t,reverse=True)) #sorted(t,reverse=True) sorts the tuple in reverse of Natural ordering i.e Descending
print(t1)

t=(10,56,987,15,46,32)
print(min(t)) #returns the minimum value in tuple
print(max(t)) #returns the maximum value in tuple

#Tuple packing and unpacking
a=10
b=20
c=30
d=65
t=(a,b,c,d)
print(type(t),t)

#unpacking

t1=(10,65,98,74)
print(t1)
x,y,z,p=t1
print("x=",x,"y=",y,"z=",z,"p=",p)

