#program to enter name and percentage of marks in dict and display info.
n=int(input("Enter the number of students:"))
rec={}
i=0
while i<n:
	name=input("Enter the name of student:")
	marks=input("Enter the marks of student in percentage:")
	rec[name]=marks
	i=i+1
print("Name of the Student","\t","Marks of Student in %")
for x in rec:
	print("\t",x,"\t\t",rec[x])