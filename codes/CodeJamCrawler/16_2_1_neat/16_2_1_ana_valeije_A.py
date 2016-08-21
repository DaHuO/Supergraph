import sys	

digits_str = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

def add_number(n, phone_digits, phone_str):
	phone_digits.append(str(n))
	for letter in digits_str[n]:
		phone_str = phone_str.replace(letter, '', 1)
	return phone_str

def get_phone_number(phone_str):
	phone_digits = []
	while phone_str:
		if 'Z' in phone_str:
			phone_str = add_number(0, phone_digits, phone_str)
		elif 'N' in phone_str and 'V' not in phone_str and 'I' not in phone_str:
			phone_str = add_number(1, phone_digits, phone_str)
		elif 'W' in phone_str:
			phone_str = add_number(2, phone_digits, phone_str)
		elif 'H' in phone_str and 'G' not in phone_str:
			phone_str = add_number(3, phone_digits, phone_str)
		elif 'U' in phone_str:
			phone_str = add_number(4, phone_digits, phone_str)
		elif 'V' in phone_str and 'F' in phone_str:
			phone_str = add_number(5, phone_digits, phone_str)
		elif 'X' in phone_str:
			phone_str = add_number(6, phone_digits, phone_str)
		elif 'N' in phone_str and 'V' in phone_str:
			phone_str = add_number(7, phone_digits, phone_str)
		elif 'G' in phone_str:
			phone_str = add_number(8, phone_digits, phone_str)
		else:
			phone_str = add_number(9, phone_digits, phone_str)

	phone_digits.sort()
	return ''.join(phone_digits)

def solveCase(case, f, fout):
	phone_str = f.readline().strip()
	phone_number = get_phone_number(phone_str)
	writeLine(fout, case, str(phone_number))

def writeLine(fout, n, result):
	print("Case #%d: %s\n" %(n, result))
	fout.write("Case #%d: %s\n" %(n, result))

if __name__ == '__main__':
	
	inputFileName = 'A-large.in'
	
	f = file(inputFileName)
	fout = file("%s.out" %(inputFileName.split(".")[0]), "w")
	
	T = eval(f.readline())
	
	for case in xrange(T):
		solveCase(case + 1, f, fout)
		
	f.close()
	fout.close()
