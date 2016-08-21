def main(): 
	
	first_input = int(input())
	user_input = int(input())
	
	if first_input >= 100:
		first_input = 100
		
	for n in range(first_input):
		x = 1
		found_answer = False
		j = 1
		input_list=[]
		while j <= 1000000 and found_answer != True:
			
			i = 1
			
			new_input = user_input * x
			
			input_string = str(new_input)

			if user_input != 0:
			
				for i in range(len(input_string)):
					number = input_string[i:i+1]
					input_list.append((number))
			
			found_0 = False
			found_1 = False
			found_2 = False
			found_3 = False
			found_4 = False
			found_5 = False
			found_6 = False
			found_7 = False
			found_8 = False
			found_9 = False
	
			for i in range(len(input_list)):
				if input_list[i] == '0': 
					found_0 = True
				elif input_list[i] == '1': 
					found_1 = True
				elif input_list[i] == '2': 
					found_2 = True
				elif input_list[i] == '3': 
					found_3 = True
				elif input_list[i] == '4': 
					found_4 = True
				elif input_list[i] == '5': 
					found_5 = True
				elif input_list[i] == '6': 
					found_6 = True
				elif input_list[i] == '7': 
					found_7 = True
				elif input_list[i] == '8': 
					found_8 = True
				elif input_list[i] == '9': 
					found_9 = True
			
			final_answer = 0
			
			if (found_0 == True) and (found_1 == True) and (found_2 == True) and (found_3 == True) and (found_4 == True) and (found_5 == True) and (found_6 == True) and (found_7 == True) and (found_8 == True) and (found_9 == True):
				final_answer = new_input
				found_answer = True
				
			j+= 1
			x+=1
			
		if found_answer == True:
			print("Case #", n+1, ": ", final_answer, sep = '')
		else:
			print("Case #", n+1, ": INSOMNIA", sep = '')
			
		if n == (first_input - 1):
			continue
		else:	
			user_input = int(input())
	
main()