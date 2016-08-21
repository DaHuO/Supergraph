import itertools, sys

with open(sys.argv[1], 'r') as file, open('out', 'w') as out:
    data = file.read().split()

    T = int(data.pop(0))

    for i in range(T):
        word = data.pop(0)
	
	wordList = list(word)
	curr = wordList.pop(0)
	ans = []
	ans.append(curr)
	for c in wordList:
		if c >= ans[0]:
			ans.insert(0, c)
		else:
			ans.append(c)
	
        out.write("Case #" + str(i+1) + ": " + ''.join(ans) + "\n")
