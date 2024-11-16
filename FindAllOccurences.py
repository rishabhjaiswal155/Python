#program to display the positions of all occurences of SubString in main String
s=input("Enter Some String:")
sub=input("Enter some subString to search:")
pos=-1
n=len(s)
flag=False
while True:
	pos=s.find(sub,pos+1,n)
	if pos==-1:
		break
	print("substring",sub,"found at index",pos,"of String",s)
	flag=True
if flag==False:
	print("subString",sub,"Not found in String",s)
	