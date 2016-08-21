def make(seq, C):
	K = len(seq)
	KG = "G"*K
	orig = seq
	for i in range(C-1):
		nx = []
		for j in seq:
			if j == "L":
				nx.append(orig)
			else:
				nx.append(KG)
		seq = "".join(nx)
	return seq
	
def solve(K, C):
	b = sum(K**i for i in range(C))
	return [(b*i) for i in range(K)]
		
def sel(s, p):
	return "".join(s[i] for i in p)
	
print "LLLL", sel(make("LLLL", 3), solve(4,3))
print "LLLG", sel(make("LLLG", 3), solve(4,3))
print "LLGL", sel(make("LLGL", 3), solve(4,3))
print "LLGG", sel(make("LLGG", 3), solve(4,3))
print "LGLL", sel(make("LGLL", 3), solve(4,3))
print "LGLG", sel(make("LGLG", 3), solve(4,3))
print "LGGL", sel(make("LGGL", 3), solve(4,3))
print "LGGG", sel(make("LGGG", 3), solve(4,3))

print "GLLL", sel(make("GLLL", 3), solve(4,3))
print "GLLG", sel(make("GLLG", 3), solve(4,3))
print "GLGL", sel(make("GLGL", 3), solve(4,3))
print "GLGG", sel(make("GLGG", 3), solve(4,3))
print "GGLL", sel(make("GGLL", 3), solve(4,3))
print "GGLG", sel(make("GGLG", 3), solve(4,3))
print "GGGL", sel(make("GGGL", 3), solve(4,3))
print "GGGG", sel(make("GGGG", 3), solve(4,3))

# LGLGGGLGL


	
print solve(4, 3)
