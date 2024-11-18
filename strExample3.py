#Program having requirement to take input as a4k3b2 and print output as aeknbd.
input=input("Enter some String:")
output=''
for x in input:
	if x.isalpha():
		output=output+x
		previous=x
	elif x.isdigit():
		output=output+chr(ord(previous)+int(x))
print("output:",output)