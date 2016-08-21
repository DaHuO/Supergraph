def countSheep(z):
	count = 1
	answer = False
	numberNeeded = {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'}

	if z == 0:
		return 'INSOMNIA'
	else:
		while True:
			y = str(count * z)
			for x in range(len(y)):
				if y[x] in numberNeeded:
					del numberNeeded[y[x]]

			if not numberNeeded:
				return y
				break

			count += 1

if __name__ == '__main__':
	t = int(raw_input())
	if 1 <= t <= 100:
		for i in xrange(1, t + 1):
	  		testInput = int(raw_input())
	  		if 0 <= testInput <= 10**6:
	  			print "Case #{}: {}".format(i, countSheep(testInput))