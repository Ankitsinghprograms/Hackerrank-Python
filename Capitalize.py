def solve(s): #Function
	list=s.split(" ")#Spluting s in list
	capitalized_word=[] #Capitalized_word list
	for each_word in list: #loop
	
		capital_word=each_word.capitalize()#capitalizing word
		
		capitalized_word.append(capital_word)#Adiing capital word in list
		
	return " ".join(capitalized_word) #join " " in list
	