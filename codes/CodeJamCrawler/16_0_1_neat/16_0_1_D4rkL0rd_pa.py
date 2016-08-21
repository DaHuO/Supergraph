def main():
	t = int(raw_input())
	for i in range(t):
		n = int(raw_input())
		if n==0:
			print "Case #{}: INSOMNIA".format(i+1)
			continue
		res = get_result(n)
		print "Case #{}: {}".format(i+1, res)

def get_result(n):
	map = {}
	ctr = 0
	tmp = n
	i = 1
	while ctr < 10:
		while tmp > 0:
			digit = tmp % 10
			tmp = int(tmp / 10)
			if digit not in map:
				ctr = ctr + 1
				map[digit] = True
		i = i + 1
		tmp = i * n
	i = i - 1
	return i * n
			

if __name__=='__main__':
	main()
