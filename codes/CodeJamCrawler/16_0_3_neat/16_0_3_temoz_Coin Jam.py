from math import sqrt
import sys

# from http://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console
def printProgress(iterations, total, prefix = '', suffix = '', decimals = 2, barLength = 100):
	"""
	Call in a loop to create terminal progress bar
	@params:
		iterations  - Required  : current iteration (Int)
		total       - Required  : total iterations (Int)
		prefix      - Optional  : prefix string (Str)
		suffix      - Optional  : suffix string (Str)
	"""
	filledLength    = int(round(barLength * iterations / float(total)))
	percents        = round(100.00 * (iterations / float(total)), decimals)
	bar             = '#' * filledLength + '-' * (barLength - filledLength)
	sys.stdout.write('%s [%s] %s%s %s\r' % (prefix, bar, percents, '%', suffix)),
	sys.stdout.flush()
	if iterations == total:
		print("\n")

def coinCandidatesSpecial(size):
	current = 0
	maxSize = pow(2, (size - 2) // 2)
	while current < maxSize:
		half = (bin(current).split('b')[-1]).zfill((size - 2) // 2)
		yield '1' + half + half[::-1] + '1'
		current += 1

def jamCoins(size, count):
	coins = {}
	remaining = count
	for number in coinCandidatesSpecial(size):
		printProgress(count - remaining, count, prefix = 'Progress')
		if remaining == 0:
			return coins
		divisors = []
		for base in range(2, 11):
			if (int(number, base) % (base + 1)) == 0:
				divisors.append(base + 1)
			else:
				divisors.append(None)
		if all(divisors):
			coins[number] = divisors
			remaining -= 1
	return coins

def main():
	fname = input()
	with open(fname) as f:
		with open('coin-out.txt', 'w') as w:
			lines = f.readlines()
			i = 1
			for line in lines[1:]:
				l = line.strip().split(' ')
				size = int(l[0])
				count = int(l[1])
				w.write("Case #%i:\n%s" % (i, 
					'\n'.join([key + ' ' + ' '.join([str(div) for div in val]) for key, val in jamCoins(size, count).items()])
					))
				i += 1

main()