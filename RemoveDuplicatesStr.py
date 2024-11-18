#Program to take input as a String from keyboard and remove the duplicates present in the string.
s=input("Enter some String:")
l=[]
for x in s:
	if x not in l:
		l.append(x)
print("output:",''.join(l))
