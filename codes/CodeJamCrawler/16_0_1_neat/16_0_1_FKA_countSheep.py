#import sys

# Open file to read
f = open ( "A-small-attempt0.in" , 'r')

# Function: Reset all seen flags
def reset_all_digits(seen_dict):
	for i in range(0, 10):
		seen_dict[str(i)] = False

#----------------------------

# Function All Digits named
def all_digits_named(seen_dict):
	for i in seen_dict:
		if seen_dict[str(i)] is False:
			return False
	return True
#----------------------------

# Function: Mark digits seen
def mark_digits(N, digits_seen):
	if N == 0:
		return 0
	copy = N
	while( copy > 0 ):
		if copy < 10:
			digits_seen[ str(copy) ] = True
			copy = copy /10
		else:
			temp = copy % 10
			copy = copy / 10
			digits_seen[ str(temp) ] = True
#----------------------------------

# Dict to keep track of all digits seen so far
digits_seen = {}

#Function name_numbers
def name_numbers(N):
	NCopy = N
	i = 1
	while True:
		mark_digits(NCopy, digits_seen)
		if all_digits_named(digits_seen):
			return str(NCopy)
		NCopy = N * i
		i +=1
#------------------------
		
		

# Read first line
line = f.readline()
total_cases = int(line)


# Start

for i in range(1, total_cases+1):
	reset_all_digits(digits_seen)
	N = int(f.readline())
	if N == 0:
		result = "INSOMNIA"
	else:
		result = name_numbers(N)
	print "Case #"+str(i)+": "+ result
	
f.close()



