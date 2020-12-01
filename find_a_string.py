def count_substring(string, sub_string):
	
	times=0
	
	length_start=0
	
	length_end=len(sub_string)
	
	for i in range (0,len(sub_string)):

		if string[length_start:length_end] ==sub_string:
			
			times+=1
		
		length_start+=len(sub_string)
		
		length_end+=len(sub_string)
		
	return times
