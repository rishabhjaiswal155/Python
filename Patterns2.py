'''Program to print pattern like
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
'''
n=int(input("Enter number of rows:"))
for i in range(1,n+1):
    i=1
    for j in range(n):
        print(i,end="")
        i=i+1
    print()
        