import pdb

infile = 'B-large.in'
outfile = 'b.out'

def flip(cake, i):
	"""flip starting at the ith pancake from the top, 0-indexed"""
	f = cake[i::-1].replace("+", "a")
	f = f.replace("-", "+")
	f = f.replace("a", "-")
	return f + cake[i+1:]
	
global cakedict
cakedict = {'-':1}


def score(cake):
	#pdb.set_trace()
	if cake in cakedict.keys():
		return cakedict[cake]
		
	else:
		
		if "-" in cake:
			neg = cake[::-1].index("-")
		else:
			return 0
		if neg != 0:
			c = cake[:-neg]
		else:
			c = cake
			
		if c == '-':
			return(1)
			
		res = []
		for s in range(1, len(c)):
			left = c[:s]
			right = c[s:]
			left = left.replace("+", "a")
			left = left.replace("-", "+")
			left = left.replace("a", "-")
			res.append(score(left) + score(flip(right, len(right) - 1)))
	
	ret = min(res) + 1
	cakedict[cake] = ret
	return ret
	
def solve():
	with open(infile, 'r') as f, open(outfile, 'w+') as out:
		T = int(f.readline())
		for i in range(T):
			N = f.readline()
			ans = score(N[:-1])
			out.write("Case #{0}: {1}\n".format(i +1, ans))
			
if __name__ == '__main__':
	solve()
			
		
		
