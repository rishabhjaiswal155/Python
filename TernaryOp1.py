#use of Ternary Operator to find the minimum number
a=int(input("Enter the first number:"))
b=int(input("Enter second number:"))
min=a if a<b else b
print("Minimum number:",min)

#use of Ternary Operator with 'and' logical operator to find the maximum number
x=int(input("Enter the first number:"))
y=int(input("Enter the second number:"))
z=int(input("Enter the Third number:"))
max=x if x>y and x>z else y if y>z else z
print("Maximum number:",max)

#use of nested Ternary Operator to find if two numbers are either equal,greater,smaller
p=int(input("Enter the first number:"))
q=int(input("Enter the second number:"))
print("Both numbers are equal" if p==q else "p is greater than q" if p>q else "p is smaller than q")
