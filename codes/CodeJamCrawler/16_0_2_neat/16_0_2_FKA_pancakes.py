#import sys
import time

# Function: All pancakes correct
def all_pancakes_correct(pancakes):
	for i in pancakes:
		if i == '-':
			return False
	return True
#----------------------------

# Function: All pancakes not correct
def all_pancakes_not_correct(pancakes):
	for i in range(0, len(pancakes)):
		if pancakes[i] == '+':
			return False
	return True
#----------------------------

# Function: Get last minus
def get_last_minus_index(mystr):
	for i in reversed( range (0, len(mystr))):
		if mystr[i] == '-':
			return i
#--------------------------

# Function: Get Next Index
def get_next_index(mystr):
	starting_char = mystr[0]
	if starting_char == '+':
		for i in range(1, len(mystr)):
			if mystr[i] == '-':
				for j in range(i, len(mystr)):
					if mystr[j] == '+':
						return j-1
				return len(mystr) -1
	else:
		for i in range(1, len(mystr)):
			if mystr[i] == "+":
				return i-1
			else:
				continue
		return len(mystr) -1
#--------------------------


# Function: solve by flipping
def solve_by_flipping(mystr):
	total_flips = 0
	while not all_pancakes_correct(mystr):
		#index = get_last_minus_index(mystr)
		index = get_next_index(mystr)
		'''
		if index == 0:
			if mystr[index] == '-': 
				total_flips = total_flips + 1
				#mystr[index] = '+'
				print 'replace all'
				mystr = mystr.replace("-","+")
		elif index > 0:'''
		total_flips = total_flips + 1
		first_half = mystr[:index+1]
		second_half = mystr[index+1:]
		if all_pancakes_not_correct(first_half):
			first_half = first_half.replace("-","+")
			mystr = first_half + second_half
		else:
			mystr = first_half[::-1] + second_half
	return total_flips


'''
# Function: Perform Flippings
def transform_to_custom_form(mystr):
	transformed_string = ""
	for ch in mystr:
		if transformed_string == "":
			transformed_string += ch
		else:
			ts_len = len(transformed_string)
			if transformed_string [ts_len-1] == ch:
				continue
			else:
				transformed_string = transformed_string + ch
	return transformed_string
#--------------------------------
'''

'''
#Function: truncate_faces
def truncate_faces(mystr):
	index = 0
	for i in reversed(range (0, len(mystr))):
		if mystr[i] == '+':
			index = i-1
			continue
		else:
			index = i
			break
	if index < 0:
		return ""
	else:
		return mystr[:index+1]
#--------------------------
'''

# Open file to read
f = open ( "input.txt" , 'r')

# Read first line
line = f.readline()
total_cases = int(line)


# Start
for i in range(1, total_cases+1):
	line =  f.readline()
	line = line.rstrip('\n')
	#print "line: \""+ line+"\""
	result = solve_by_flipping(line)	
	print "Case #"+str(i)+": "+ str(result)
	
f.close()



