def wrap(string,max_width):
	
	len_start=0
	len_end=max_width
	
	text=''
	
	times=len(string)//max_width
	
	for i in range(times):
		
		a=string[len_start:len_end]
		
		len_start+=max_width
		len_end+=max_width
		
		text+=a+"\n"

	else:
		
		a=string[len_start:len_end]
		
		text+=a
		
		
	return text
