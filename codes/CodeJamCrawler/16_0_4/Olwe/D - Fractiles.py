def generateMatrixByColumns(K, C):
	if C <= 1:
		for i in range(K):
			yield [True if (x & (1 << i)) != 0 else False for x in range(0, 1 << K)];
	else:
		subgen = generateMatrixByColumns(K, C - 1);
		submatrix = [];
		for i in range(C):
			for j in range(K):
				submatrix.append(next(subgen));
			for j in range(K):
				yield [submatrix[(i * C + j) // (K ** (C - 1))][x] or submatrix[(i * C + j) % (K ** (C - 1))][x] for x in range(0, 1 << K)];

def chooseTiles(S, columnGenerator, ambiguousRows, goldMatrix, start=0):
	if len(ambiguousRows) == 1:
		return [], ambiguousRows;
	if S <= 0:
		return None, ambiguousRows;
	i = start;
	while True:
		if i >= len(goldMatrix):
			try:
				goldMatrix.append(next(columnGenerator));
			except StopIteration:
				break;
		tempAmbiguousRows = ambiguousRows.copy();
		usefulColumn = False;
		for j in ambiguousRows:
			if goldMatrix[i][j]:
				usefulColumn = True;
				tempAmbiguousRows.remove(j);
		if usefulColumn:
			tiles, tempAmbiguousRows = chooseTiles(S - 1, columnGenerator, tempAmbiguousRows, goldMatrix, i + 1);
			if tiles != None and len(tempAmbiguousRows) == 1:
				return [i] + tiles, tempAmbiguousRows;
		i += 1;
	return None, ambiguousRows;

numCases = int(input());
for case in range(1, numCases + 1):
	K, C, S = input().split(' ');
	K = int(K);
	C = int(C);
	S = int(S);
	if S >= K:
		print("Case #" + str(case) + ":", ' '.join(str(x) for x in range(1, K + 1)));
		continue;
	tiles, _ = chooseTiles(S, generateMatrixByColumns(K, C), set(range(1 << K)), []);
	if tiles == None:
		print("Case #" + str(case) + ": IMPOSSIBLE");
	else:
		print("Case #" + str(case) + ":", end=' ');
		for tile in tiles[:-1]:
			print(tile + 1, end=' ');
		print(tiles[-1] + 1);
