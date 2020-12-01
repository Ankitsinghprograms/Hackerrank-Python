def split_and_join(line):	 
	 word=""	 
	 for letter in line:
	 	if letter==" ":
	 		word=word+"-"
	 	else:
	 		word=word+letter
	 return word