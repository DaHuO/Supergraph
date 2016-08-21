import sys

def getWinningAnswer(s):
	ans = ""
	for c in s:
		if len(ans) == 0:
			ans += c
			continue
		if c < ans[0]:
			ans = ans + c
		else:
			ans = c + ans
	return ans

infile = open(sys.argv[1], "r")
outfile = open("answer.out", "w")

skip = True
n = 1
for line in infile:
	if skip:
		skip = False
		continue
	outfile.write("Case #" + str(n) + ": " + getWinningAnswer(line))
	n += 1

print("done")