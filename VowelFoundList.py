#Program to display unique vowels and its count present in the given word.
vowels=['a','e','i','o','u']
found=[]
word=input("Enter Some String:")
for letter in word.lower():
	if letter in vowels:
		if letter not in found:
			found.append(letter)
print("Unique Vowels found in word is:",found,"and its count is:",len(found))
			

