def parseFile(f):
	pairs = []
	for line in f:
		buff = line.strip().split(' ')
		first = buff.pop(0)
		second = buff.pop(0)
		pairs.append ( ([first, second], buff) )
	return pairs

def mergePairs(pairs, nWords, nPairs):
	i = 0
	printed = set()
	while True:
		pair = pairs[i]
		divs = ' '.join(pair[1])
		for j in range(nWords):
			for k in range(nWords):
				for l in range(nWords):
					for t in range(nWords):
						word = pair[0][j % 2] + pair[0][k % 2] + pair[0][l % 2] + pair[0][t % 2]
						if word not in printed:
							print(word + ' ' + divs)
							printed.add(word)
							if len(printed) == nPairs: return
		i += 1

def main():
	f = open('C-large.in', 'r')
	t = int(f.readline().strip())
	n,j = [int(x) for x in f.readline().strip().split(' ')]
	###
	db = open('pairs.dat', 'r')
	pairs = parseFile(db)
	db.close()
	###
	print("Case #1:")
	mergePairs(pairs, n // 8, j)
	
if __name__ == '__main__':
	main()