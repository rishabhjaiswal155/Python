#Program to print unique vowels and number of vowels present in the word using intersection()

word=input("Enter some word:")
s=set(word)
v={'a','e','i','o','u'}
s1=s.intersection(v)
print("Unique vowels present in the word",word,"is:",s1)
print("The number of vowles present in the word is:",len(s1))
