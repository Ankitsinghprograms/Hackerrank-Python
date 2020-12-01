n=[]
l=[]
c=0
i=int(input())
count=[]
while i>c:
	a=input()
	l.append(a)
	c+=1
print(len(set(l)))
for each in l:
	if each in n:
		continue
	else:
		count.append(l.count(each))
		n.append(each)
print(*count)


