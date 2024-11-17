#program to display the positions of all occurences of SubString in main String,Also count number of occurences
s=input("Enter Some String:")
sub=input("Enter some subString to search:")
pos=-1
n=len(s)
flag=False
count=0
while True:
    pos=s.find(sub,pos+1,n)
    if pos==-1:
        break
    flag=True
    count+=1
    print("substring",sub,"found at index:",pos)
if flag==False:
    print("substring",sub,"not found in String",s)
print("Number of Occurence are:",count)