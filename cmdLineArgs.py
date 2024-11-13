#Command Line Arguments
from sys import argv
print(type(argv))
print(argv[1:])

#To find the number of Command line arguments passed
from sys import argv
args=argv[1:]
print("Length of argv:",len(args))

#Printing command line argumnts one by one
from sys import argv
print("Printing command line arguments one by one")
for x in argv[1:]:
  print(x)