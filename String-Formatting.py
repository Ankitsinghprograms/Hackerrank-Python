def decimal(number):
	return number

def octal(number):#octal
	sum=""
	
	while number>=8:
		
		remainder=number%8
		number=number//8
		sum=sum+str(remainder)
	else:
		sum+=str(number)
		
	return sum[::-1]

def hexadecimal(number):#hexadecimal
	sum=""
	
	while number>=16:
		
		remainder=number%16
		
		if remainder==10:
			remainder="A"
		
		elif remainder==11:
			remainder="B"
			
		elif remainder==12:
			remainder="C"
		
		elif remainder==13:
			remainder="D"
		
		elif remainder==14:
			remainder="E"
			
		elif remainder==15:
			remainder="F"
		
		
		number=number//16
		sum=sum+str(remainder)
	else:
		sum+=str(number)
		
	return sum[::-1]

def binary(number):#binary
	sum=""
	
	while number>=2:
		
		remainder=number%2
		number=number//2
		sum=sum+str(remainder)
	else:
		sum+=str(number)
		
	return sum[::-1]


		
def print_formatted(number):
	
	times=0
	for i in range(1,number+1):
		
		if times==0:
		
			print(f" {decimal(i)}  {octal(i)}  {hexadecimal(i)}  {binary(i)}")
		else:
			print(f" {decimal(i)}  {octal(i)}  {hexadecimal(i)} {binary(i)}")
			
			times+=1
#For test

#a=print_formatted(17)
