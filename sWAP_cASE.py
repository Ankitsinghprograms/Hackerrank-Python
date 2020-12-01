def swap_case(s):
	
	swapped_word=""
	
	for letter in s:
		
		if letter.isupper():
			swapped_letter=letter.lower()
			
		elif letter.islower():
			swapped_letter=letter.upper()
		else:
			swapped_letter=letter
		swapped_word=swapped_word+swapped_letter


	return swapped_word
		
	