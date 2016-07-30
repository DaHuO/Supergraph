T = int(raw_input())

def stack(c):
	if c == 'P':
		return 'PR'
	if c == 'S':
		return 'PS'
	if c == 'R':
		return 'RS'

def simulate(N, given):
	out = given
	for i in xrange(N):
		new = ""
		for ch in out:
			new += stack(ch)
		out = new
	return new

#import Queue

def fix(tt, N):
	operate = list(tt)
	for i in xrange(N):
		new = []
		while len(operate) > 0:
			a = operate.pop()
			b = operate.pop()
			if a > b:
				new.append(b+a)
			else:
				new.append(a+b)
		new.reverse()
		operate = new
	return operate


def doprob():
	read = raw_input().split()
	N = int(read[0])
	R = int(read[1])
	P = int(read[2])
	S = int(read[3])

	legit = []

	t1 = simulate(N, 'R')

	if t1.count('R') == R:
		if t1.count('P') == P:
			if t1.count('S') == S:
				legit.append(t1)

	t2 = simulate(N, 'P')

	if t2.count('R') == R:
		if t2.count('P') == P:
			if t2.count('S') == S:
				legit.append(t2)

	t3 = simulate(N, 'S')

	if t3.count('R') == R:
		if t3.count('P') == P:
			if t3.count('S') == S:
				legit.append(t3)

	if len(legit) == 0:
		return "IMPOSSIBLE"	
	legit = [fix(tt, N)[0] for tt in legit]	
	return sorted(legit)[0]

for qq in xrange(T):
	print "Case #" + str(qq+1) + ": " + str(doprob())