def LetterOrder(letter):
	return ord(letter) - ord('A')

def algo(line):
	return_letters = ''
	last_letter_order = 0
	for letter in line:
		current_letter_order = LetterOrder(letter)
		if(current_letter_order >= last_letter_order):
			return_letters = letter + return_letters
			last_letter_order = current_letter_order
		else:
			return_letters = return_letters + letter
	return return_letters

if __name__ == '__main__':
	
	fout = open('A-large.out', 'w')

	with open('A-large.in','r') as fin:
		number_of_cases = fin.readline()
	
		case = 1
		for line in fin.readlines():
			#print(line)
			ans = algo(line.strip())
			fout.write("Case #{0}: {1}\n".format(str(case), ans))
			case += 1

	fout.close()
