def counting_sheep(N):
	lst = [0] * 10
	count = 0
	index = 1
	number = index * N

	if N == 0:
		return "INSOMNIA"
	
	while count < 10:
		str_num = str(number)
		for ch in str_num:
			if lst[int(ch)] == 0:
				lst[int(ch)] += 1
				count += 1
		index += 1
		number = index * N
	return (index - 1) * N

def main():
	f = open('sheep_input.txt', 'r')
	output = open('sheep_output.txt', 'w')
	T = f.readline()
	for i in range(1,int(T)+1):
		N = int(f.readline())
		number = counting_sheep(N)
		if str(number).isdigit():
			output.write("Case #%d: %d\n" %(i, number))
		else:
			output.write("Case #%d: INSOMNIA\n" % i)
	f.close()
	output.close()
