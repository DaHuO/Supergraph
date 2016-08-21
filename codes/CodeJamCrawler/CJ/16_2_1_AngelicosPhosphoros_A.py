import string

alphabet = string.ascii_uppercase

#print alphabet



unics_digits = {"Z":0, "W": 2, 'U':4, 'G':8, 'X':6}

digits = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

order = [0,2,4,6,8,1,5,9,3,7]

def check_exist(string, counts):
	#print "check_exist %s"%s
	for x in string:
		if not counts[x]:
			#print x
			return False
	return True

def decrease(string, counts):
	for x in string:
		counts[x] = counts[x]-1

def get_number_of_digit(dig, counts):
	ret = 0
	while check_exist(digits[dig],counts):
		ret+=1
		decrease(digits[dig],counts)
	return ret


def proceed_string(s):
	char_numbers = dict()
	for ch in alphabet:
		char_numbers[ch] = 0
	for ch in s:
		char_numbers[ch] = char_numbers[ch]+1
	#print char_numbers
	counts = [0]*10
	for x in order:
		counts[x] = get_number_of_digit(x,char_numbers)
	#print counts
	ret_string = ""
	for i in xrange(10):
		nums =  [i]*counts[i]
		ret_string+="".join(str(x) for x in nums)
	return ret_string

T = input()
out = ""
for i in xrange(T):
	s = raw_input()
	out +="Case #%d: %s\n"%(i+1, proceed_string(s))

print out[0:len(out)-1]

def output():
	f = open("output.txt","w")
	f.write(out)
	f.close()

#output()