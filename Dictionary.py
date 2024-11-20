#Dictionary data structure

#Creating dictionary objects

#using empty dict {}

d={}
print(type(d),d)

#using dict object:

d=dict()
print(type(d),d)

#using known elements
d={100:'Rishabh',101:'Vishal',102:'Amol'}
print(type(d),d)

#Adding the element in dictionary using d[key]=value:

d[103]='Shreyash'
print(d)

#Accessing dictionary element using key:
print(d[103])

