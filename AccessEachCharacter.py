#Program to access each character of string in forward as well as backward direction
#using slice operator
s=input("Enter String:")
print("String in forward Direction is",s[:])
print("String in Backward direction is",s[-1:-(len(s)+1):-1])

#using while loop
#for positive index in forward manner
s=input("Enter String:")
i=0
print("String in forward Direction with positive index is")
while i<=len(s)-1:
	print(s[i],end='')
	i+=1
print()

#using while loop
#for positive index in backward manner
s=input("Enter String:")
i=len(s)-1
print("String in backward Direction with positive index is")
while i>=0:
	print(s[i],end='')
	i-=1
print()

#using while loop
#for negative index in forward manner
s=input("Enter String:")
i=-(len(s))
print("String in forward Direction with negative index is")
while i<=-1:
	print(s[i],end='')
	i+=1
print()

#using while loop
#for negative index in backward manner
s=input("Enter String:")
i=-1
print("String in backward Direction with negative index is")
while i>=(-len(s)):
	print(s[i],end='')
	i-=1
print()