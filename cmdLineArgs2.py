#Read a group of int values from keyboard as Command line arguments and print its sum.
from sys import argv
args=argv[1:]
sum=0
for x in args:
    n=int(x)
    sum+=n
print("The sum of command line arguments:",sum)

#Loop holes in command line arguments
from sys import argv
print(argv[1]+argv[2])#Default type of argv items is str so it concatenates the two str
print(int(argv[1])+int(argv[2]))#Type cast it as int and prints the sum
print(argv[7:1000])#prints empty list as it takes slice operaator valid
print(argv[1000])#Gives error as 1000 index is not there

