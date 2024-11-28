#random module and its varoius functions in python

from random import *
print("printing random float values between 0 and 1 not inclusive:")
for i in range(10):
	print(random()) #random() returns the float values between 0 and 1 not inclusive.
print("printing random int values between 1 and 100 inclusive:")
for i in range(10):
	print(randint(1,100)) #randint(1,100) returns the int values between 1 and 100 inclusive.
print("printing random float values between 1 and 100 not inclusive:")
for i in range(10):
	print(uniform(1,100)) #uniform(1,100) returns the float values between 1 and 100 not inclusive.
print("printing random int values between some range(start,stop,step):")
for i in range(10):
	print(randrange(1,100,2)) #randrange(1,100,2) returns the int values between 1 and 99 with step value of 2.
#Default value for start=0 step=1

list=['Rishabh','Vishal','Amol','Shreyash','Lucky']
print("printing random names from the list:")
for i in range(10):
	print(choice(list)) #return the random object either from list or tuple collection.
	