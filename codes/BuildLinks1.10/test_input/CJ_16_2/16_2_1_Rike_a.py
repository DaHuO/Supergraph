file = open("C:\\Users\\Rike\\Documents\\GoogleCodeJam\\a.in", "r")
output = open("C:\\Users\\Rike\\Documents\\GoogleCodeJam\\output.txt", "w")

num_cases = int(file.readline())

def is_cont(stringi, numbers):
	is_cont = True
	for letter in stringi:
		if(numbers[letter] == 0):
			is_cont =  False
		numbers[letter] = numbers[letter] - 1
	if not is_cont:
		for letter in stringi:
			numbers[letter] = numbers[letter] + 1
	return is_cont

for i in range(num_cases):
	output.write("Case #" + repr(i + 1) + ": ")
	word = file.readline().strip()
	
	numbers = {}
	
	for letter in "ZWOURFXSVIGHTNIE":
		numbers[letter] = word.count(letter)
	final_num = {"1":0, "2" :0, "3" : 0, "0" : 0, "4" : 0, "5" : 0, "6" :0, "7":0, "8":0, "9":0}
	outfilestr = ''
	while(is_cont("SIX", numbers)):
		final_num["6"] =  final_num["6"] + 1
	while(is_cont("SEVEN", numbers)):
		final_num["7"] =  final_num["7"] + 1
	while(is_cont("FIVE", numbers)):
		final_num["5"] =  final_num["5"] + 1
	while(is_cont("FOUR", numbers)):
		final_num["4"] =  final_num["4"] + 1
	while(is_cont("ZERO", numbers)):
		final_num["0"] =  final_num["0"] + 1
	while(is_cont("TWO", numbers)):
		final_num["2"] =  final_num["2"] + 1
	while(is_cont("ONE", numbers)):
		final_num["1"] =  final_num["1"] + 1
	while(is_cont("NINE", numbers)):
		final_num["9"] =  final_num["9"] + 1
	while(is_cont("THREE", numbers)):
		final_num["3"] =  final_num["3"] + 1
	while(is_cont("EIGHT", numbers)):
		final_num["8"] =  final_num["8"] + 1
	outfilestr = ''	
	for i in range(final_num["0"]):
		outfilestr = outfilestr + "0"
	for i in range(final_num["1"]):
		outfilestr = outfilestr + "1"
	for i in range(final_num["2"]):
		outfilestr = outfilestr + "2"
	for i in range(final_num["3"]):
		outfilestr = outfilestr + "3"
	for i in range(final_num["4"]):
		outfilestr = outfilestr + "4"
	for i in range(final_num["5"]):
		outfilestr = outfilestr + "5"
	for i in range(final_num["6"]):
		outfilestr = outfilestr + "6"
	for i in range(final_num["7"]):
		outfilestr = outfilestr + "7"
	for i in range(final_num["8"]):
		outfilestr = outfilestr + "8"
	for i in range(final_num["9"]):
		outfilestr = outfilestr + "9"
	
	print(numbers)
	output.write(outfilestr + "\n")
output.close()
file.close()