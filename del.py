#del keyword and None data type
s="Rishabh"
s1="Rishabh"
s2="Rishabh"
del s1,s2
print(s)
#print(s1)#Error as s1 is undefined because varaible s1 and s2 is deleted and object is marked for Garbage Collection

#None data type
s=10
y=None
del s
print(y)