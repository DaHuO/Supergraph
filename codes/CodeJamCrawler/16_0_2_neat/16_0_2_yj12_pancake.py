def solve(line):
    prev = line[0]
    count = 0
    for i in line[1:]:
	if prev != i:
	    count += 1
	    prev = i
    if line[-1] == '-':
	count += 1
    return count


file = 'B-large.in'
cases = []
with open(file) as f:
    f.readline()
    for line in f.readlines():
	cases.append(line.strip())

f = open('pancake.large.out', 'w')
for i, c in enumerate(cases):
    f.write('Case #' + str(i+1) + ': ' + str(solve(c)) + '\n')

f.close()