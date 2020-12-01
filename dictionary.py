
dic={}

scores=[]
for _ in range(int(input())):
	name = input()
	score = float(input())
	
	if score in dic.keys():
	
		dic[score].append(name)
		
	else:
		scores.append(score)
	
		dic.update({score:[name]})
	
	
scores.sort(reverse=True)

lowest_marks_list=dic.get(scores[-2])

lowest_marks_list.sort()

lowest_marks=lowest_marks_list

for each_student in lowest_marks:
	print(each_student)

