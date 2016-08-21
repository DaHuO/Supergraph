from itertools import permutations

def is_subseq(x, y):
    it = iter(y)
    return all(any(c == ch for c in it) for ch in x)

def prmv(y,s):
	for i in y:
		a = s.replace(i,"",1)
		s = a
	return s

def solve(s):
	scopy = s
	d = ["ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE","ZERO"]
	df = {"ONE":1,"TWO":2,"THREE":3,"FOUR":4,"FIVE":5,"SIX":6,"SEVEN":7,"EIGHT":8,"NINE":9,"ZERO":0}
	ans = []
	L = 0

	while "Z" in s:
		z = [''.join(p) for p in permutations("ZERO")]
		# print z
		for y in z:
			if is_subseq(y,s):
				ans.append("ZERO")
				s = prmv(y,s)
				L += 4


	while "X" in s:
		z = [''.join(p) for p in permutations("SIX")]
		# print z
		for y in z:
			if is_subseq(y,s):
				ans.append("SIX")
				s = prmv(y,s)
				L += 3

	while "W" in s:
		z = [''.join(p) for p in permutations("TWO")]
		# print z
		for y in z:
			if is_subseq(y,s):
				ans.append("TWO")
				s = prmv(y,s)
				L += 3

	while "G" in s:
		z = [''.join(p) for p in permutations("EIGHT")]
		# print z
		for y in z:
			if is_subseq(y,s):
				ans.append("EIGHT")
				s = prmv(y,s)
				L += 5
	while "U" in s:
		z = [''.join(p) for p in permutations("FOUR")]
		# print z
		for y in z:
			if is_subseq(y,s):
				ans.append("FOUR")
				s = prmv(y,s)
				L += 4

	while "H" in s:
		z = [''.join(p) for p in permutations("THREE")]
		# print z
		for y in z:
			if is_subseq(y,s):
				ans.append("THREE")
				s = prmv(y,s)
				L += 5

	while "O" in s:
		z = [''.join(p) for p in permutations("ONE")]
		# print z
		for y in z:
			if is_subseq(y,s):
				ans.append("ONE")
				s = prmv(y,s)
				L += 3


	while "F" in s:
		z = [''.join(p) for p in permutations("FIVE")]
		# print z
		for y in z:
			if is_subseq(y,s):
				ans.append("FIVE")
				s = prmv(y,s)
				L += 5


	while "S" in s:
		z = [''.join(p) for p in permutations("SEVEN")]
		# print z
		for y in z:
			if is_subseq(y,s):
				ans.append("SEVEN")
				s = prmv(y,s)
				L += 5

	while "N" in s:
		z = [''.join(p) for p in permutations("NINE")]
		# print z
		for y in z:
			if is_subseq(y,s):
				ans.append("NINE")
				s = prmv(y,s)
				L += 4
	# print s
	while s != "":
		# print s
		for x in d:
			z = [''.join(p) for p in permutations(x)]
			# print z
			for y in z:
				if is_subseq(y,s):
					ans.append(x)
					s = prmv(y,s)
					L += len(x)

	realans = []
	for a in ans:
		realans.append(df[a])


	realans.sort()
	zzz = [str(i) for i in realans]

	return "".join(zzz)
	



	 

def dosolve(f,g):
	d = f.read().split("\n")
	n = int(d[0])

	j = 1
	for i in range(1,n+1):
		print "\n Case no " + str(i) + "\n"
		print solve(d[i])
		g.write ("Case #" + str(i) + ": " + str(solve(d[i])) + "\n")

	return 0

def solve_large():
	g = open("A-large-out.txt","w")
	f = open("A-large.in","r")
	dosolve(f,g)

def solve_small():
	g = open("A-small-out-4.txt","w")
	f = open("A-small-attempt4.in","r")
	dosolve(f,g)

def solve_examples():
	g = open("A-eg-out.txt","w")
	f = open("A-eg.in","r")
	dosolve(f,g)
	
# solve_examples()
# solve_small()
solve_large()

# solve("OZONETOWER")