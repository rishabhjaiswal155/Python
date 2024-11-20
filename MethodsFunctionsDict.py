#Methods and Functions of Dictionary

d=dict()
print(type(d),d)

#dict() with list of tuples
d=dict([(100,'Rishabh'),(200,'Amol')])
print("dict() with list of tuples:",d)

#dict() with set of tuples
d=dict({(100,'Rishabh'),(200,'Amol')})
print("dict() with set of tuples:",d)

#dict() with tuple of tuples
d=dict(((100,'Rishabh'),(200,'Amol'),(300,'shreyash')))
print("dict() with tuple of tuples:",d)

#len()
print("Length 0f dict:",len(d))

#get(key)
k=int(input("Enter the key to search the corresponding value:"))
if k in d:
	print("value for given key:",d.get(100))
else:
	print("Key is not present in dictionary")
	
#get(key,defaultvalue)
k=int(input("Enter the key to search the corresponding value:"))
v=input("Enter the default value if key is not found:")
print(d.get(k,v))
print("After d.get(key,default value):",d)

#pop(key)
k=int(input("Enter the key to pop the corresponding value:"))
if k in d:
	print("popped value from dict:",d.pop(k))
	print("After pop(key):",d)
else:
	print("key not found in the dictionary")

#popitem() removes the random item from dict
print("After popitem():",d.popitem())
print("dict after popitem():",d)

#keys() returns all the dict-keys of dict
d1={100:'Rishabh',101:'Visahl',102:'amol'}
print("All the keys in dict:",d1.keys())

#values() returns all the dict-values of dict
d1={100:'Rishabh',101:'Visahl',102:'amol'}
print("All the values in the dict:",d1.values())

#items() returns all the dict-items of dict
d1={100:'Rishabh',101:'Visahl',102:'amol'}
print("All the items in the dict:",d1.items())

#copy() to create a new object by cloning the present object
d={100:'sunny',101:'Bunny',103:'pillu'}
d1=d.copy()
print("cloning After copy()",d1)

#setdefault()
d={100:'sunny',101:'Bunny',103:'pillu'}
d.setdefault(100,'krishu')
d.setdefault(104,'Trishu')
print("After setdefault():",d)

#update()

d={100:'sunny',101:'Bunny',103:'pillu'}
d.update({104:'vishu',105:'nillu'})
print("after update(dict):",d)
d.update([(106,'gaju'),(107,'chiku')])
print("after update(list of tupls):",d)
