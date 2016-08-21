def checkern(x):
	if x == '0':
		return "INSOMNIA"
	numbers = []

	mult = 0

	while len(numbers) != 10:
		mult+=1
		val = str(int(x) * mult)
		val = list(val)
		for i in val:
			if i not in numbers:
				numbers.append(i)
		val = "".join(val)
		
	return val


def main():
	f = open('A-large.in')
	n = int(f.readline())
	cases = []
	for i in range(n):
		cases.append(f.readline().split("\n")[0])

	f = open('out.out', 'w')
	for i in enumerate(cases):
		f.write("Case #%s: " % str(i[0]+1) + str(checkern(str(i[1])))+'\n')

if __name__ == '__main__':
	main()