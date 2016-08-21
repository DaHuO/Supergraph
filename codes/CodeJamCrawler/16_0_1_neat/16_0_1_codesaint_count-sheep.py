import sys

required = set([1,2,3,4,5,6,7,8,9,0])

def count(case, i, seen = set()):
	if case == 0:
		return "INSOMNIA"
	else:
		result = i*case
		result = map(int, list(str(result)))
		seen |= set(result)
		
		if seen == required:
			return i*case
		else:
			i+=1
			return count(case, i, seen)

cases = 0
for i, line in enumerate(sys.stdin):
	if i == 0:
		cases = int(line.strip())
	elif i <= cases:
		print "Case #%d: %s"  % (i, str(count(int(line.strip()), 1, set())))
