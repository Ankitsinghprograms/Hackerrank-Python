k=int(input())

list_of_room=input().split()

check_rooms=[]

for each_room in list_of_room:
	
	if each_room in check_rooms:
		continue
		
	no_of_same_rooms=list_of_room.count(each_room)
	
	if no_of_same_rooms==1:#Captain room
	
		print(each_room)
		break
		
	else:
		
		check_rooms.append(each_room)
		
		