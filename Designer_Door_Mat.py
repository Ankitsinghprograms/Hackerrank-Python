a=input().split(" ")
n=int(a[0])
m=int(a[1])


first=(m-3)//2
second=1
times=0

while times<n:

	if times<n//2:
		
		print(first*"-",second*".|.",first*"-",sep="")
		
		first-=3
		second+=2

	elif times>n//2:

		print(first*"-",second*".|.",first*"-",sep="")
		
		first+=3
		second-=2

	else:
		pattern=(m-7)//2
		
		print(pattern*"-","WELCOME",pattern*"-",sep="")
		
		first+=3
		second-=2

	times+=1
	