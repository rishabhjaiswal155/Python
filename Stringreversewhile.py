#Program to reverse the given string using while loop
s="Rishabh Full stack Developer"
i=len(s)-1
output=''
while i>=0:
	output=output+s[i]
	i-=1
print(output)
