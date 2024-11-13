#form-1(without any args used for new line character) and form-2(with str as arg) of output statements
print("Hello,Rishabh")
print()
print("How are You!!")
print("Rishabh\nJaiswal")#'\n' like escape operators can be used
print("Rishabh"+"Jaiswal") #'+' with both str args treated as concatenation
print("Rishabh"*3) #'*' as repeatation operator having one str and other int arg
print("Rishabh","Jaiswal") #',' treat as space

#form-3(with variable number of args)
a,b,c,d=10,20,30,"Rishabh"
print("The values are:",a,b,c,d)

#sep,end atttributes of print()
print(a,b,c,d)#default seperator is space
print(a,b,c,d,sep=':')#sep attribute
print("Rishabh",end='....')#end attribute
print("Jaiswal")


