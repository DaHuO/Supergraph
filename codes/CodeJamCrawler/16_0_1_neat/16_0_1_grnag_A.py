# 2016 qualifying round. problem A - counting sheep

inFile =  open("A.large.in", "r")

T = int(inFile.readline().split()[0])

case = 1

def get_digits(N):
	res = []
	M = N
	count = 1
	if N == 0:
		return 0, "INSOMNIA"
	while True:
		N = M*count
		while N > 0:
			rem = N % 10
			if rem not in res:
				res.append(N%10)
			N = N/10

			#print "---", res
			if len(res) == 10:
				return res, M * count
		count += 1

while case <= T:
	N = int(inFile.readline().split()[0])
	A, B = get_digits(N)
	
	print "Case #{}: {}".format(case, B)
	case += 1
