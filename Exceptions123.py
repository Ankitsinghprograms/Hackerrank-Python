for i in range(int(input())):
	
	user=input().split(" ")
	
	try:
		a=int(user[0])
		b=int(user[1])
	
	
		print(a//b)
		
	except Exception as error:
		
		print("Error Code:",error)
		
