from math import sqrt; from itertools import count, islice

def base(innitvar,basevar,convertvar):
	SY2VA = {'0': 0,
			'1': 1,
			'2': 2,
			'3': 3,
			'4': 4,
			'5': 5,
			'6': 6,
			'7': 7,
			'8': 8,
			'9': 9,
			'A': 10,
			'B': 11,
			'C': 12,
			'D': 13,
			'E': 14,
			'F': 15,
			'G': 16,
			'H': 17,
			'I': 18,
			'J': 19,
			'K': 20,
			'L': 21,
			'M': 22,
			'N': 23,
			'O': 24,
			'P': 25,
			'Q': 26,
			'R': 27,
			'S': 28,
			'T': 29,
			'U': 30,
			'V': 31,
			'W': 32,
			'X': 33,
			'Y': 34,
			'Z': 35,
			'a': 36,
			'b': 37,
			'c': 38,
			'd': 39,
			'e': 40,
			'f': 41,
			'g': 42,
			'h': 43,
			'i': 44,
			'j': 45,
			'k': 46,
			'l': 47,
			'm': 48,
			'n': 49,
			'o': 50,
			'p': 51,
			'q': 52,
			'r': 53,
			's': 54,
			't': 55,
			'u': 56,
			'v': 57,
			'w': 58,
			'x': 59,
			'y': 60,
			'z': 61,
			'!': 62,
			'"': 63,
			'#': 64,
			'$': 65,
			'%': 66,
			'&': 67,
			"'": 68,
			'(': 69,
			')': 70,
			'*': 71,
			'+': 72,
			',': 73,
			'-': 74,
			'.': 75,
			'/': 76,
			':': 77,
			';': 78,
			'<': 79,
			'=': 80,
			'>': 81,
			'?': 82,
			'@': 83,
			'[': 84,
			'\\': 85,
			']': 86,
			'^': 87,
			'_': 88,
			'`': 89,
			'{': 90,
			'|': 91,
			'}': 92,
			'~': 93}

	integer = 0
	for character in innitvar:
		assert character in SY2VA, 'Found unknown character!'
		value = SY2VA[character]
		assert value < basevar, 'Found digit outside base!'
		integer *= basevar
		integer += value

	VA2SY = dict(map(reversed, SY2VA.items()))

	array = []
	while integer:
		integer, value = divmod(integer, convertvar)
		array.append(VA2SY[value])
	answer = ''.join(reversed(array))

	return answer	
	
def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))
    
def factor(n):
	for i in xrange(2,n/2):
		if(n%i==0):
			return i

k = 0
for i in xrange(32768,65535):
	if(isPrime(i)==True):
		continue
	flag = 0
	ans = base(str(i),10,2)
	if(ans[0]!='1' or ans[-1]!='1'):
		continue
	for j in xrange(3,11):
		b = base(ans,j,10)
		if(isPrime(int(b))==True):
			flag = 1
			break
	if(flag==0):
		print ans,
		k = k+1
		for j in xrange(2,11):
			b = base(ans,j,10)
			c = factor(int(b))
			print c,
		print 
	if(k==50):
		break

