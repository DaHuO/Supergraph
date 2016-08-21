def countingSheep(N):
	digits = [0] * 10
	number = N
	if number == 0:
		return 'INSOMNIA'
	else:
		while sum(digits) < 10:
			listedN = map(int, str(number))
			for x in listedN:
				digits[x] = 1
			number += N
		return number - N


def main():
	fileName = raw_input()
	with open(fileName) as f:
		rawFile = f.read()
	info = rawFile.split()
	info = map(int, info)
	numTests = info[0]
	for i in range(numTests):
		print "Case #"+str(i+1)+': '+ str(countingSheep(info[i+1]))


if __name__ == "__main__":
    main()