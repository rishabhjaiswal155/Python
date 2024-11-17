#Program to print the charcters at odd position and even position for the given String.
#using slice operator

s="Rishabh"
print("input string:",s)
print("charcters at even position are:",s[::2])
print("charcters at odd position are:",s[1::2])

#using while loop

i=0
print("chaarcters at even position are:")
while i<len(s):
	print(s[i],end='')
	i+=2
print()

i=1
print("chaarcters at odd position are:")
while i<len(s):
	print(s[i],end='')
	i+=2