from math import sqrt

def getdivisor(num):
	if num == 2:
		return None
	elif num == 3:
		return None
	elif num % 2 == 0:
		return 2
	elif num < 9:
		return None
	elif num % 3 == 0:
		return 3
	else:
		r = int(sqrt(num))
		d = 5
		while d <= r and d < 5000:
			if num % d == 0:
				return d
			if num % (d + 2) == 0:
				return d + 2
			d += 6
		return None

def getResult(coin):
	nlist = [int(coin, i) for i in range(2, 11)]
	dlist = list()
	for i in nlist:
		divisor = getdivisor(i)
		if divisor is None:
			return
		else:
			dlist.append(divisor)
	return dlist

def main():
	with open('outbig.txt', 'w') as outfile:
		n = 32
		j = 500
		samples = 0
		a = '1' * (n - 2)

		outfile.write('Case #1:\n')
		for i in range(int(a, 2) + 1):
			coin = '1' + '{0:b}'.format(i).zfill(n - 2) + '1'
			dlist = getResult(coin)
			if dlist is not None:
				print(coin, dlist)
				outfile.write('{0} '.format(coin) + ' '.join(map(str, dlist)) + '\n')
				samples += 1
			if samples >= j:
				break

if __name__ == '__main__':
	main()