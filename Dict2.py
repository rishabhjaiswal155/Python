#Program to find the number of occurences of each letter present in the given String.

s=input("Enter some String:")
d={}
for x in s:
	d[x]=d.get(x,0)+1
for k,v in sorted(d.items()):
	print("{} occured {} times".format(k,v))
