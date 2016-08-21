def count(s):
	s = s.rstrip('+')
	if not s:
		return 0
	num = int(s[-1] == '-')
	for i in range(1, len(s)):
		num += s[i] != s[i-1]
	return num

f = open('input_small.txt')

for i, line in enumerate(f):
	line = line.strip()
	if not i:
		continue
	print("Case #%i: %i" % (i, count(line)))