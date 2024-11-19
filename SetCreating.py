#set data structure
#creating set object

#all known items
s={10,20,30,40,65,45}
print(type(s),s)

#using empty set
s=set()
print(type(s),s)
s.add(10)
s.add(20)
s.add(230)
print(s)

#using set() if any sequence is given
s="Rishabh"
s1=set(s)
print(type(s1),s1)

l=[10,25,65,48,98]
s2=set(l)
print(type(s2),s2)

r=range(1,21)
s2=set(r)
print(type(s2),s2)