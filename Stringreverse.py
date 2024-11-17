#Program to reverse the given string
#using slice operator
s="Rishabh Full stack developer"
print("string reverse using slice operator:")
for x in s[::-1]:
	print(x,end='')
print()

#using reversed() which returns reverse object and end attribute. 
s="Rishabh Full stack developer"
print("String reverse using reversed():")
for x in reversed(s):
    print(x,end='')
print()

#using reversed()and join()
s="Rishabh Full stack developer"
print("string reverse using reversed() and join()")
for x in reversed(s):
    print(' '.join(x),end='')
    
    