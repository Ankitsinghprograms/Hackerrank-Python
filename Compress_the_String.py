
#import time

s=list(input())
#a=time.time()
times=1
place=0
for i in range(len(s)):

	for n in s:
		if place<(len(s)-1):	
			if s[place]==s[place+1]:
				times+=1
				place+=1
	if place<(len(s)):
		print((times,int(s[place])),end=" ")
		times=1
		place+=1
		
#b=time.time()
#print(b-a)