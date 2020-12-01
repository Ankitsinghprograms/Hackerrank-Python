l=[]

for i in range(int(input())):
	
	n=input()
	
	n=n.split(" ")
	
	function=n[0]
	
	if len(n)>1:
		statement=int(n[1])
	
	#Changing every value of list into integer
	
	l=list(map(int,l))
	
	#insert
	if function=="insert":
			
		statement_2=n[2]
			
		l.insert(int(statement),statement_2)
	
	#print
	elif function=="print":
			
			print(l)
	
	#Remove
	elif function=="remove":
			
			l.remove(statement)
	
	#Append
	elif function=="append":
		
			
			l.append(statement)
	
	#Sort
	elif function=="sort":
			
			l.sort(reverse=False)
	
	#pop
	elif function=="pop":
			
			if len(n)>1:#If pop is used to remove any specific place
				
				l.pop(statement)
				
			else:#pop will remove last place value
			
				l.pop()
	
	#Reverse			
	elif function=="reverse":
			
		l.reverse()
			
	else:#Error
		
		continue
		