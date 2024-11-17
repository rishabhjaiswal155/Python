#Program having requirement to take input as B4A1D3 and print output as ABD134

input=input("Enter some String:")
s1=s2=output=''
for x in input:
	if x.isalpha():
		s1=s1+x
	else:
		s2=s2+x
for x in sorted(s1):
	output=output+x
for y in sorted(s2):
	output=output+y
print("output:",output)
	
		
	