#Program to reverse the given string using while loop
s="Rishabh Full stack Developer"
i=len(s)-1
output=''
while i>=0:
	output=output+s[i]
	i-=1
print(output)

#Program to take input as "Rishabh Full Stack Developer" and print output as "Developer Stack Full Rishabh"
input="Rishabh Full Stack Developer"
print("input:",input)
l=input.split()
l1=[]
i=len(l)-1
while i>=0:
    l1.append(l[i])
    i-=1
print("output:",' '.join(l1))

#Program to take input as "Rishabh Full Stack Developer" and print output as "hbahsiR lluF kcatS repoleveD".
input="Rishabh Full Stack Developer"
print("input:",input)
l=input.split()
l1=[]
for x in l:
    l1.append(x[::-1])
output=' '.join(l1)
print("output:",output)
