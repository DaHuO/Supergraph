start = input();

for T in range(int(start)):
	combination = input();
	reqMoves = 0;
	newString = [];
	for x in range(len(combination)):
		newString.append(combination[x]);

	reqMoves = len(newString);
	if combination.endswith("+"):
		reqMoves = reqMoves - 1;

	doubling = 0;
	for x in range(len(newString) - 1):
		if newString[x] == newString[x+1]:
			doubling += 1;

	reqMoves = reqMoves - doubling;
	print ("Case #%s: %s" %((T + 1), reqMoves))