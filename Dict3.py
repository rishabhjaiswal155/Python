#Program to print the number of occurences of each vowel present in the given String.

word=input("Enter some word:")
vowels=['a','e','i','o','u']
d={}
for x in word:
	if x in vowels:
		d[x]=d.get(x,0)+1
for k,v in sorted(d.items()):
	print("{} occured {} times".format(k,v))

