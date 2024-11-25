#Variable length argument

#Program to find the sum of all variables where number of variable are not known

def sum(*n):
	result=0
	for x in n:
		result=result+x
	print("The sum is:",result)
sum()
sum(10)
sum(10,20,30,40,50)

#Variable length argument with positional argument

def sum(name,*n):
	result=0
	for x in n:
		result=result+x
	print("The sum by",name,"is:",result)
sum("Rishabh") #variable length argument must be last argument if used with positional argument
sum("Vishal",10)
sum("Ravi",10,20,30,40,50)

#Keyword variable length argument

def student(**kwargs): #Here type(kwargs) is dict
    for k,v in kwargs.items():
        print(k,".....",v)
student()
student(name="Rishabh",age=28,marks=92,course="PG_DAC")
student(name="Rishabh",lan1="Java",lan2="python",lan3="C#")
