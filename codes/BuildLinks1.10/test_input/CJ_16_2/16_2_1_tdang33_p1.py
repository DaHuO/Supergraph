
import sys

def gcd(x,y):
	if y == 0:
		return x
	else:
		return gcd(y, x%y)

def power2(y):
	if (y == 1):
		return True
	if (y % 2 != 0):
		return False
	return power2(y/2)

def output(x,y):
	if 2*x >= y:
		return 1
	else:
		return 1 + output(x, y/2)

def count (s):
	cW = 0
	cZ = 0
	cU = 0
	cF = 0
	cG = 0
	cH = 0
	cV = 0
	cS = 0
	cI = 0
	cO = 0
	for i in s:
		if i == 'W':
			cW += 1
		elif i == 'Z':
			cZ += 1
		elif i == 'U':
			cU += 1
		elif i == 'F':
			cF += 1
		elif i == 'G':
			cG += 1
		elif i == 'H':
			cH += 1
		elif i == 'V':
			cV += 1
		elif i == 'S':
			cS += 1
		elif i == 'I':
			cI += 1
		elif i == 'O':
			cO += 1	

	return cW, cZ, cU, cF, cG, cH, cV, cS, cI, cO

in_ = sys.stdin
sys.stdin = open('A-large.in', 'r')
#sys.stdin = open('input1.txt', 'r')
#sys.stdin = open('A-small-attempt0.in', 'r')
out = sys.stdout
sys.stdout = open('output1.txt', 'w')

T = int(raw_input())

for case in range(1,T+1):
	s = raw_input()
	#s = ''.join(sorted(s))
	cW, cZ, cU, cF, cG, cH, cV, cS, cI, cO = count(s)
	two = cW
	zero = cZ
	four = cU
	five = cF - four
	eight = cG
	three = cH - eight
	seven = cV - five
	six = cS - seven
	nine = cI - five - six - eight
	one = cO - two - four - zero
	ans = '0'*zero + '1'*one + '2'*two + '3'*three + '4'*four + '5'*five + '6'*six + '7'*seven + '8'*eight + '9'*nine
	print "Case #{}: {}".format(case, ans)

sys.stdin = in_
sys.stdout = out