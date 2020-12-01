input=input()
b=0
for i in input:
	if i=="0" or i=="1" or i=="2" or i=="3" or i=="4" or i=="5" or i=="6" or i=="7" or i=="8" or i=="9":
		i=int(i)
		b+=i

	else:
		continue
print(b)