inpath = "A-large.in"
outpath = "res1-large.out"

def theLastWord(s):
	res = s[0]
	for i in range(1, len(s)):
		if s[i] >= res[0]:
			res = s[i] + res[:]
		else:
			res += s[i]
	return res

out = open(outpath, 'w')
args = []
with open(inpath) as f:
    lines = f.readlines()[1:]
    for line in lines:
    	args.append(line.strip())

for i in range(len(args)):
	res = theLastWord(args[i])
	out.write("Case #{}: {}\n".format(i + 1, res))