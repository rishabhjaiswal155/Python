#comparision Operaator like >,>=,<,<= and Equality operator likes ==,!= in str
#program to accept two string from keyboard and check whether it is equal,greater or smaller amongst them.

s=input("Enter String1:")
s1=input("Enter String2:")
if s==s1:
	print("Both String",s,"and",s1,"are equal")
elif s>s1:
	print("String",s,"is greater than",s1)
elif s<s1:
	print("String",s,"is smaller than",s1)
	