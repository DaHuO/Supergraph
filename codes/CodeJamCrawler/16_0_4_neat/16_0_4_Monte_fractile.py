#Fractiles

def increment(s):
	res = ""
	for i in reversed(range(len(s))):
		if s[i] == 'G':
			res = 'L' + res
			res = s[:i] + res
			return res
		else:
			res = 'G' + res

def transform(s, c,original):
	if c == 1:
		return s

	res = ""
	for ch in s:
		if ch == 'L':
			res += original
		else:
			res += k*'G'
	return transform(res,c-1,original)


		
num = int(raw_input())

for i in range(1, num+1):
	k,c,s = [int(x) for x in raw_input().split(' ')]

	if s >= k:
		out = "Case #{0}:".format(i)
		for index in range(s):
			out += " {0}".format(index+1)
		print out
		continue

	st = 'G'*k

	counts = [0]*k**c

	for j in range(2**k):
		t = transform(st,c,st)
		for index in range(len(t)):
			if t[index] == 'L':
				counts[index] += 1
		st = increment(st)

	needed = min(counts)

	if needed > s:
		print "Case #{0}: IMPOSSIBLE".format(i)
		continue
	# print counts
	out = "Case #{0}:".format(i)
	found = 0

	for index in range(len(counts)):
		if counts[index] == needed:
			out += " {0}".format(index+1)
			found += 1
		if found == needed:
			break
	print out







