def produceTileData(k, c):
	tileCount = pow(k,c)
	affectTile = int(tileCount / k)

	kData = [0 for i in range(k)]

	tileData = [0 for i in range(tileCount)]
	tileDataList = []
	tileDataList.append(tileData)

	while 0 in kData:
		number = int(''.join([ "%d"%x for x in kData]), 2) + 1
		number = int(bin(number)[2:])

		kData = list(map(int,str(number)))
		while len(kData) < k:
			kData.insert(0, 0)
		tileData = []
		for i in range(k):
			if kData[i] == 0:
				data = [0 for i in range(affectTile)]
			if kData[i] == 1:
				data = [kData[n % len(kData)] for n in range(affectTile)]
			tileData += data
		tileData = list(tileData)
		tileDataList.append(tileData)

	# print("\n".join(" ".join(str(el) for el in row) for row in tileDataList))
	return tileDataList

t = int(input())
for i in range(1, t + 1):
	k, c, s = [int(s) for s in input().split(" ")]

	# tileData = produceTileData(k, c)

	print("Case #{}: ".format(i), end=' ')
	for count in range(s):
		if (2*s) <= k:
			print("IMPOSSIBLE", end=' ')
			break
		if s == k:
			print("{}".format(count+1), end=' ')
		else:
			print("{}".format(count+2), end=' ')
		
	print()
