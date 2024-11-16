#Membership operators (in,not in) in str
s=input("Enter some String:")
s1=input("Enter subString to search:")
if s1 in s:
	print("subString",s1,"is present in String",s)
else:
	print("subString",s1,"is not present in String",s)