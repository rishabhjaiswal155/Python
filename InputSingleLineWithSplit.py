#Read multiple values from the keyboard in a single line
a,b=[int(x)for x in input("Enter two numbers:").split()]
print(a)
print(b)

#Read multiple values from the keyboard which are speecified with ',' seperation and print sum in a single line
a,b=[float(x)for x in input("Enter two numbers:").split(',')]
print("The Sum:",a+b)


