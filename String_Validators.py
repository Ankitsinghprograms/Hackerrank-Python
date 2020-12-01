s=input()
l=list(s)

a=0
b=0
c=0
d=0
e=0

for i in l:
	
	if i.isalnum():
		a+=1

	if i.isalpha():
		b+=1

	if i.isdigit():
		c+=1

	if i.islower():
		d+=1

	if i.isupper():
		e+=1

		
	
if a>0:
	print(True)
else:
	print(False)

if b>0:
	print(True)
else:
	print(False)
	
if c>0:
	print(True)
else:
	print(False)
	
if d>0:
	print(True)
else:
	print(False)
	
if e>0:
	print(True)
else:
	print(False)