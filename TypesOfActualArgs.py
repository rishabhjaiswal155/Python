#Types of actual arguments:

#Positional arguments and keyword arguments
#If we are mixing keyword and positional arguments then positional argument must be taken first in function call then keyword argument must be taken

def emp(name,age):
	print("Employee name=",name)
	print("Employee age=",age)
emp('Rishabh',28) #These are positional arguments Here the number and position of arguments is important i.e name='Rishabh' age=28
emp(name='Rishabh',age=28) #These are keyword arguments
emp(age=29,name='surabhi') #Here the number and name of arguments is important not the position
emp('Mansi',age=25) #Combination of both positional and keyword arguments
#default arguments (Here Rule is default argument must be last parameter of function definition)
def wish(msg,name='Guest'): #Here if name is not provided in function call then default name=Guest will be taken
	print("Hello",name,msg)
wish('Good Morning')
wish('Good Evening','Rishabh') #First positional argument must be taken ,then default argument



