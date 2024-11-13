#form-1(without any args used for new line character) and form-2(with str as arg) of output statements
print("Hello,Rishabh")
print()
print("How are You!!")
print("Rishabh\nJaiswal")#'\n' like escape operators can be used
print("Rishabh"+"Jaiswal") #'+' with both str args treated as concatenation
print("Rishabh"*3) #'*' as repeatation operator having one str and other int arg
print("Rishabh","Jaiswal") #',' treat as space
print("-----------------------------")
#form-3(with variable number of args)
a,b,c,d=10,20,30,"Rishabh"
print("The values are:",a,b,c,d)
print("---------------------------------")
#sep,end atttributes of print()
print(a,b,c,d)#default seperator is space
print(a,b,c,d,sep=':')#sep attribute
print("Rishabh",end='....')#end attribute
print("Jaiswal")
print("---------------------------------------")

#print() with Object as argument
list=[10,20,30,40]
tuple=(100,200,300,400,'Rishabh')
set={1,2,3,4,'Rishabh'}
print(list,tuple,set)

print("---------------------------------")




