from sys import argv

def complify(seq, levels):
	complified = seq
	for _ in range(levels-1):
		temp = []
		for char in complified[:len(seq)]:
			if char == 'L':
				temp += seq
			else:
				temp += ['G' for _ in seq]
		complified = temp
	return complified
	
#this logic is hacked and broken
with open(argv[1], 'r') as of:
	cases = int(of.next())
	for n, x in enumerate(of):
		inp = x.strip().split()
		k = int(inp[0])
		c = int(inp[1])
		s = int(inp[2])
		
		essential_origs = [['L' for _ in range(k)] for _ in range(k)]
		essential_seqs = []
		for i in range(k):
			essential_origs[i][i] = 'G'
		for seq in essential_origs:
			compd = complify(seq, c)
			essential_seqs.append(compd)
		cols = zip(*essential_seqs)
		tiles = set([])
		row = 0
		for i, col in enumerate(cols):
			while row < len(col):
				if col[row] == 'G':
					row += 1
					tiles.add(i)
				else:
					break
		if row == len(cols[0]):
			if len(list(tiles)) <= s:
				tiles = ' '.join(str(x+1) for x in list(tiles))
			else:
				tiles = 'IMPOSSIBLE'
		else:
			tiles = 'IMPOSSIBLE'
		print('Case #' + str(n+1) + ': ' + tiles)