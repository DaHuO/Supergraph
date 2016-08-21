import sys

fin = open(sys.argv[1], 'r') if len(sys.argv) > 1 else sys.stdin

T = int(fin.readline())

def sub(key, cc, str):
	if (key in cc and cc[key] > 0):
		count = cc[key]
		for c in str:
			cc[c] -= count
		return  count
	return 0

for t in range(1, T + 1):
	W = fin.readline().rstrip()
	
	a = [0] * 10
	
	cc = dict()
	for c in W:
		cc[c] = W.count(c)
	
	a[0] = sub('Z', cc, "ZERO")
	a[2] = sub('W', cc, "TWO")
	a[6] = sub('X', cc, "SIX")
	a[8] = sub('G', cc, "EIGHT")
	a[3] = sub('H', cc, "THREE")
	a[4] = sub('R', cc, "FOUR")
	a[1] = sub('O', cc, "ONE")
	a[5] = sub('F', cc, "FIVE")
	a[7] = sub('V', cc, "SEVEN")
	a[9] = sub('I', cc, "NINE")
	
	print("Case #{0}: {1}".format(t, "".join(str(k) * v for k, v in enumerate(a))))
	