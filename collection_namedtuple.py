#from collections import namedtuple

#marks=[]

#times=int(input())

#types=input().split()
#	
#Student=namedtuple("Student",[types[0],types[1],types[2],types[3],])


#for i in range(times):

#	S_input=input().split()
#	
#	S=Student(S_input[0],S_input[1],S_input[2],S_input[3])
#	
#	marks.append(S.MARKS)
#	
#total_marks=sum(list(map(int,marks)))

#average=total_marks/times

#print(average)

from collections import namedtuple
marks=[]
times,types=int(input()),input().split()
Student=namedtuple("Student",[types[0],types[1],types[2],types[3],])
for i in range(times):
	S_input=input().split()	
	S=Student(S_input[0],S_input[1],S_input[2],S_input[3])	
	marks.append(int(S.MARKS))
print((sum(marks)/times))