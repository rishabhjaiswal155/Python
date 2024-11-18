#Program having requirement to take input as a4b3c2 and print output as aaaabbbcc.
input=input("Enter some string:")
output=''
for x in input:
	if x.isalpha():
		output=output+x
		previous=x
	elif x.isdigit():
		output=output+previous*(int(x)-1)
print("output:",output)
		