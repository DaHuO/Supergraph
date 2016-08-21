def get_vector(num, vector):
	n = list(str(num))
	for item in n:
		vector |= (1 << int(item))
	return vector

def main():
	n, i = 0, 0
	nums = []
	with open('A-large.in') as f:
		for line in f:
			if i == 0:
				n = int(line)
				i += 1
			else:
				nums.append(int(line))
	for i in xrange(n):
		vector = 0
		num, x = nums[i], nums[i]
		if num == 0: 
			print "Case #{}: INSOMNIA".format(i+1)
			continue
		j = 2
		while True:
			vector = get_vector(num, vector)
			if vector == 1023: 
				print "Case #{}: {}".format(i+1, num)
				break
			num = x * j
			j += 1

main()

