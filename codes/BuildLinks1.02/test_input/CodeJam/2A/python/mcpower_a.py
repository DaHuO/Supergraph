def do_case():
	n, r, p, s = map(int, input().split())
	"""
	n=1: winner of lower
	n=2: loser of lower
	n=3: winner of lower
	n=4: loser of lower
	"""
	if max(abs(p-r), abs(r-s), abs(s-p)) > 1:
		return "IMPOSSIBLE"
	return recurse(n, p, r, s)
	# always start with p if possible
	# first one should ALWAYS be p = big

def recurse(n, p, r, s):
	# if n == 0:
	# 	if p:
	# 		return "P"
	# 	if r:
	# 		return "R"
	# 	if s:
	# 		return "S"
	arr = [p, r, s]
	if n == 1:
		if p and r:
			return "PR"
		if r and s:
			return "RS"
		if p and s:
			return "PS"
	if arr.count(min(arr)) == 2:
		# one max
		# always take max index
		# recurses are either max/2 or max/2 - 1
		big = max(arr)//2
		out = ""
		for i in reversed(range(3)):
			if arr[i] == min(arr):
				out += recurse(n-1, *[big if j != i else big-1 for j in range(3)])
		return out
	else:
		# two max
		# recurses are 2x min/2, 1x min/2+1
		small = min(arr) / 2
		out = ""
		for i in range(3):
			if arr[i] == max(arr):
				out += recurse(n-1, *[small if j != i else small+1 for j in range(3)])
		return out


t = int(input())

for case in range(t):
	print("Case #{}:".format(case+1), do_case())
