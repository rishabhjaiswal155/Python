#functions of str
#strip(),lstrip(),rstrip()

s=input("Enter some String:")
print(s.lstrip()) #lstrip() removes the spaces from left side
print(s.rstrip()) #rstrip() removes the spaces from right side
print(s.strip())  #strip() removes the spaces from both sides.

#find(),rfind()
s1=input("Enter some String:")
sub=input("Enter sub String to search:")
print(s1.find(sub)) #find() returns the index of first occurrence of substring if found otherwise returns -1
print(s1.rfind(sub)) #rfind() returns the index of first occurrence of substring from reverse direction if found otherwise returns -1
print(s1.find(sub,5,len(s1))) #find(substring,begin,end) returns the index of substring if found with the searching range of begin to end-1,otherwise returns -1
#index()
s1=input("Enter some String:")
sub=input("Enter sub String to search:")
try:
	n=s1.index(sub)
	print("substring",sub,"found at index",n) #index() returns the index of first occurrence of substring if found otherwise returns value Error
except(ValueError):
	print("substring",sub,"not found")

#rindex()
s1=input("Enter some String:")
sub=input("Enter sub String to search:")
try:
	n=s1.rindex(sub)
	print("substring",sub,"found at index",n) #rindex() returns the index of first occurrence of substring from reverse direction if found otherwise returns value Error
except(ValueError):
	print("substring",sub,"not found")
	