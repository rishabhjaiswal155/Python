'''Program to print pattern like
*
**
***
****
***** 
'''
n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
	for j in range(i):
		print("*",end="")
	print()

'''Program to print pattern like
*****
*****
*****
*****
*****
'''
n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range(n):
        print("*",end="")
    print()

'''program to print pattern like
*****
****
***
**
*
'''
n=int(input("Enter number of rows:"))
for i in range(1,n+1):
    for j in range(i,n+1):
        print("*",end="")
    print()