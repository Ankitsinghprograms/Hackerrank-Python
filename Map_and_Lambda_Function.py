cube=lambda x:x**3

def fibonacci(n):
	
	l=[]
	
	for i in range(n):
		
		if i==0:
			l.append(0)
			
		elif i==1:
			l.append(1)
			
		else:
			l.append(l[i-2]+l[i-1])
		
	return l