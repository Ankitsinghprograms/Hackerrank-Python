if __name__ == '__main__':
    n = int(input())
    student_marks={}
	
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        
    query_name=input()
    
    get=student_marks.get(query_name)
    
    total=0
    
    no=0
    
    for marks in get:
    	
    	total=total+float(marks)
    	
    	no+=1
    	
       
    print(total/no)