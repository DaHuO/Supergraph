import itertools


dic = {}

with open("16.all", "r") as f:
	for line in f:
		if "#" in line:
			continue
		coin = line[:16]
		dvs = line [16:len(line) - 1]
		if dvs not in dic:
			dic[dvs] = [coin]
		else:
			dic[dvs].append(coin)

print "Case #1:"
count = 0

for k, v in dic.iteritems():
	if len(v) >= 2:
		for subset in itertools.combinations(v, 2):
			print subset[0] + subset[1] + k
			count += 1
			if count == 500:
				break
		if count == 500:
			break
		# pass
	else:
		print v[0] + v[0] + k
		count += 1
		if count == 500:
			break
