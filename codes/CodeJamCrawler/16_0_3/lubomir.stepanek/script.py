###############################################################################
###############################################################################
###############################################################################

## data loading

file_name = "C-small-attempt2.in"

file_pointer = open(file_name, "r")
my_strings = file_pointer.read()
file_pointer.close()


###############################################################################

## data parameters

T = my_strings.split("\n")[0]
N, J = my_strings.split("\n")[1].split(" ")

N = int(N)
J = int(J)


###############################################################################

## helper functions

def getMyNumber(my_string, my_base):
	
	output = 0
	
	for i in range(len(my_string)):
		output += int(my_string[i]) * (my_base ** (len(my_string) - 1 - i))
	
	return output


def firstNontrivialDivisor(my_number):
	
	output = False
	
	if my_number == 1:
		return False
	if my_number == 2:
		return False
	if my_number > 2:
		i = 2
		while not(output) and i <= (1.0 + int(my_number) ** 0.5):
			if my_number % i == 0:
				output = i
			i += 1
	
	return output


###############################################################################

## core computations

i = 0

possible_jamcoins = ["0", "1"]

while i <= N - 4:
	new_generation = []
	
	for item in possible_jamcoins:
		new_generation.append(item + "0")
		new_generation.append(item + "1")
	
	possible_jamcoins = new_generation
	
	i += 1


for i in range(len(possible_jamcoins)):
	possible_jamcoins[i] = "1" + possible_jamcoins[i] + "1"


###############################################################################

k = 0
my_jamcoin_indices = []
proven_divisors = []

while len(my_jamcoin_indices) < J:
	
	has_nontrivial_divisor = True
	my_divisors = []
	l = 2
	
	while has_nontrivial_divisor and l <= 10:
		
		first_nontrivial_divisor = firstNontrivialDivisor(getMyNumber(possible_jamcoins[k], l))
		
		if first_nontrivial_divisor == False:
			has_nontrivial_divisor = False
			my_divisors = []
		
		if first_nontrivial_divisor != False:
			has_nontrivial_divisor = True
			my_divisors.append(first_nontrivial_divisor)
		
		l += 1
	
	if has_nontrivial_divisor:
		my_jamcoin_indices.append(k)
		proven_divisors.append(my_divisors)
	
	k += 1


###############################################################################

my_jamcoins = []

for index in my_jamcoin_indices:
	my_jamcoins.append(possible_jamcoins[index])

output = "Case #" + T + ":" + "\n"

for i in range(J):
	row = ""
	
	for j in range(len(proven_divisors[i]) - 1):
		row += str(proven_divisors[i][j]) + " "
	row += str(proven_divisors[i][-1]) + "\n"
	
	output += str(my_jamcoins[i]) + " " + row
	
	
###############################################################################

## outputting

file_name = "C-small-attempt-out.in"

file_pointer = open(file_name, "w")
file_pointer.write(output)
file_pointer.close()


###############################################################################
###############################################################################
###############################################################################






