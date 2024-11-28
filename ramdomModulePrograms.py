#Python program to generate 6 digit random number as OTP.

from random import *
print("random 6 digit OTP:")
for i in range(10):
	print(randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),sep='')
	
#Python program to generate password of length 6 digits in which positions like 1st,3th,5th are alphabet symbols and 2nd,4th,6th are digits

from random import *
print("random 6 digit password containing alphabets at 1,3,5 th place and digits at 2,4,6 th place:")
for i in range(10):
	print(chr(randint(65,90)),randint(0,9),chr(randint(65,90)),randint(0,9),chr(randint(65,90)),randint(0,9),sep='')
	