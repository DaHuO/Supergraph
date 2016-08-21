def find_count(N):
	digits = {}
	i = 1
	res = 0
	while len(digits) != 10:
		res = i*N
		while res != 0:
			d = res % 10
			digits[d] = True
			res /= 10
		i += 1
	return (i-1)*N

def main():
	T = int(raw_input())
	for i in range(T):
		N = int(raw_input())
		out = "INSOMNIA"
		if N != 0:
			out = find_count(N)
		print "Case #{0}: {1}".format(i+1, out)

if __name__ == '__main__':
	main()
