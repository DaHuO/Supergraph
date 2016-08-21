import sys
T = case = -1
file = open(sys.argv[1], 'r')

digits=["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

def rec(f, d):
	f0 = f[:]
	i = d
	while i<10:
		f = f0[:]
		found = True
		for c in digits[i]:
			if f[ord(c)-ord('A')]==0:
				found = False
				break
			f[ord(c)-ord('A')] -= 1
		if found:
			if sum(f)==0: return True,str(i)
			okli, res2 = rec(f, i)
			if okli:
				return True, str(i) + res2
		i+=1
	return False,'0'

for x in file:
	x = x.strip()
	case += 1
	if case==0:
		T = int(x)
		continue
	f = [0]*26
	for c in x: f[ord(c)-ord('A')]+=1
	okli,res = rec(f, 0)
	print 'Case #%d:' % case, res
	if case==T:
		break
