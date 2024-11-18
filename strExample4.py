#Program having requirement to take input two strings like s1='RAVI' s2='TEJA' and print output as 'RTAEVJIA'.
s1=input("Enter First String:")
s2=input("Enter Second String:")
i=j=0
output=''
while i<len(s1) or j<len(s2):
	if i<len(s1):
		output=output+s1[i]
	if j<len(s2):
		output=output+s2[j]
	i+=1
	j+=1
print("output:",output)
	