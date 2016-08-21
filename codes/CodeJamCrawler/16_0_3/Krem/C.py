import sys

T = sys.stdin.readline()
T = int(T)

def findDiv(x):
	for i in range(2,min(300,x-1)):
		if x % i == 0:
			return i
	return 0

for i in range(0,T):
	line = sys.stdin.readline().split()
	N = int(line[0])
	J = int(line[1])
	found = 0
	cand = [0] * N
	cand[0] = 1
	cand[N-1] = 1
	sys.stdout.write("Case #" + str(i+1) +":\n")
	while found < J:
		good_stuff = []
		for I in range(2,11):
			num = 0
			pot = 1
			for i in range(0,N):
				num += cand[i]*pot
				pot *= I
			r = findDiv(num)
			if (r == 0):
				break
			good_stuff = good_stuff + [r]
		if len(good_stuff) == 9:
			found += 1
			for i in reversed(range(0,N)):
				sys.stdout.write(str(cand[i]))
			sys.stdout.write(" ")
			for x in good_stuff:
				sys.stdout.write(str(x))
				sys.stdout.write(" ")
			sys.stdout.write("\n")
		for i in range(1, N-2):
			if cand[i] == 0:
				cand[i] = 1
				break
			else:
				cand[i] = 0
