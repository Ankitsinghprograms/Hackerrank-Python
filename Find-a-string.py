
#Hard method but Its very important to learn Problem solving and logical reasoning This is best problem for logical reasoning and problem solving

def count_substring(string,sub_string):
	
	times=0
	
	new_string=string[0:]
	
	for i in range(len(string)):
		
		find_substring=new_string.find(sub_string)
		
		
		if find_substring>=0:
			
			times+=1
			
			new_string= new_string[1+find_substring:]
			
	return times
		

#a=count_substring("abcab","ab")
#print(a)

#Easy method via function count

#def count_substring(string,sub_string):
#	times=string.count(sub_string)
#	return times
#	
#a=count_substring("abcdabcd","abc")
#print(a)

#One liner

#def count_substring(string,sub_string):
#	return string.count(sub_string)
	