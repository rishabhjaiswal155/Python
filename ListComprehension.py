#List Comprehension syntax: l=[Expression for x in sequence if condition]

#Program to print the squares of number between 1-20 in List

l=[x*x for x in range(1,21)]
print(l)

#Program to print the 2 to power of number where number is between 1-10 in List

l=[2**x for x in range(1,11)]
print(l)

#program to print square of number between range of 1-20 if te number is odd.
l=[x*x for x in range(1,21) if (x*x)%2!=0]
print(l)

#Program to print the first character of each word in the list
words=['Rishabh','Jaiswal','IACSD','SGGS']
l=[w[0] for w in words]
print(l)

#Program to print the word only if its length >5
words=['Rishabh','Raj','Rama','Vishal','Shreyash']
l=[w for w in words if len(w)>5]
print(l)

#program to print the items of List1 only which are not there in list2.
n1=[10,20,30,40,50]
n2=[30,40,50,60,70]
l=[x for x in n1 if x not in n2]
print(l)

#Print the each words in sequence in uppercase and its length 
words='The quick brown fox jumps over the lazy dog'
print(words)
words=words.split()
print(words)
l=[[w.upper(),len(w)]for w in words]
print(l)