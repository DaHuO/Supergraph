def cari(num):
	mem, digit = {}, [0]*10
	base = 0
	while True:
		base += num
		if base in mem: 
			return "INSOMNIA"
		mem[base] = True
		basecp = base
		while basecp:
			digit[basecp%10] = 1
			basecp /= 10
		if sum(digit) == 10: break
	return base

t = int(raw_input())
for c in range(1, t+1):
	inp = int(raw_input())
	print "Case #{}: {}".format(c, cari(inp))