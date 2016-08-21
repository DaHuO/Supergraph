t = int(raw_input())

def get_lineup(n,r,p,s):
	if abs(r-p) <= 1 and abs(r-s) <= 1 and abs(p-s) <= 1:
		if n == 1:
			seq = ""
			if p == 1:
				seq += "P"
			if r == 1:
				seq += "R"
			if s == 1:
				seq += "S"
			return seq
		else:
			if r > s and r > p:
				return get_lineup(n-1, r/2,p/2+1,s/2) + get_lineup(n-1, r/2,p/2,s/2+1)
			if s > r and s > p:
				return get_lineup(n-1, r/2,p/2+1,s/2) + get_lineup(n-1, r/2+1,p/2,s/2)
			if p > r and p > s:
				return get_lineup(n-1, r/2+1,p/2,s/2) + get_lineup(n-1, r/2,p/2,s/2+1)
			if r < s and r < p:
				return get_lineup(n-1, r/2,p/2+1,s/2) + get_lineup(n-1, r/2,p/2,s/2+1)
			if s < r and s < p:
				return get_lineup(n-1, r/2,p/2+1,s/2) + get_lineup(n-1, r/2+1,p/2,s/2)
			if p < r and p < s:
				return get_lineup(n-1, r/2+1,p/2,s/2) + get_lineup(n-1, r/2,p/2,s/2+1)

	else:
		return "IMPOSSIBLE"

for i in range(t):
	[n,r,p,s] = map(int, raw_input().split(" "))
	print "Case #" + str(i+1) + ": " + get_lineup(n,r,p,s)