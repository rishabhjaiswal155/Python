#Replacing old String with new String replace(old,new) 
s="Learning python is very easy, beacuse of its consice code"
print(s.replace("easy","difficult"))

#splitting of string using split(seperator) default value of seperator is space
print(s.split())#It returns the list of String
print(s.split(','))
print(s.split(' ',4)) #It returns the list of String with max limit of 4,default value of max limit is -1
print(s.rsplit(' ',4))

#join() of str to join string in given list or tuple syntax: 'seperator'.join(list or tuple)
l=['Rishabh','Jaiswal','IACSD','Pune','PG-DAC']
print(':'.join(l))
t=('Rishabh','Jaiswal','IACSD','Pune','PG-DAC')
print('-'.join(t))

