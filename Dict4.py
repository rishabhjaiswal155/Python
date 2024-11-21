#Program to accept the name of student and his marks from keyboard in dictionary.Also display student marks by taking student name as input.

n=int(input("Enter the number of students:"))
d={}
for x in range(n):
	name=input("Enter the name of student:")
	marks=int(input("Enter the marks of student:"))
	d[name]=marks
print("The record of students is:",d)
while True:
	name=input("Enter the name of student to find the marks:")
	marks=d.get(name,-1)
	print("The marks of student {} is {}".format(name,marks))
	if marks==-1:
		print("student not found")
	option=input("Do you want to find the marks of other student:[Y|N]:")
	if option=='N':
		break
print("Thanks for using this Application.....")
	
	