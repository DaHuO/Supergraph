import string

def answer(s, p):
	parties = list(string.ascii_uppercase)[0:s]
	rst = []
	total = sum(p);
	escape = []
	while total:
		if len(escape) == 2:
			rst.append(''.join(escape))
			escape = []
		i = p.index(max(p))
		p[i] -= 1
		total -= 1
		escape.append(parties[i])
	rst.append(''.join(escape))
	if len(rst[-1]) == 1:
		rst[-1], rst[-2] = rst[-2], rst[-1]
	return ' '.join(rst)






T = int(raw_input())

for t in range(1, T+1):
    s = int(raw_input())
    p = [int(x) for x in raw_input().split(' ')]
    print "Case #" + str(t) + ": " + answer(s, p)
