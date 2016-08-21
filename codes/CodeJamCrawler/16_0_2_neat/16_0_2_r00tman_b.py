def flip(s, i):
	return ''.join([{'+':'-', '-':'+'}[c] for c in s[:i+1]])+s[i+1:]

def solve(s):
	was = {s}
	dist = {s: 0}
	q = [s]
	while q:
		c = q[0]
		del q[0]
		for i in range(len(c)):
			nc = flip(c, i)
			if nc not in was:
				was.add(nc)
				dist[nc] = dist[c]+1
				q.append(nc)

	res = dist['+'*len(s)]
	return res

with open("output.txt", "w") as f:
    for i,l in enumerate(open("B-small-attempt0.in").readlines()[1:]):        
        res = solve(l.strip())
        print('Case #{}: {}'.format(i+1, res), file=f)
