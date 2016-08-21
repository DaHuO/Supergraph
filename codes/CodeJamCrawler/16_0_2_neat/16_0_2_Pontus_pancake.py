fname = 'B-large.in'
fin  = open(fname, 'r')
fout = open('out.txt','w')
T = int(fin.readline().strip())
case = 1
for l in fin:
	pancakes = l.strip()
	sections = 1
	last_pancake = pancakes[0]
	for p in pancakes:
		if not p == last_pancake:
			last_pancake = p
			sections += 1
	if pancakes[-1] == '+':
		fout.write('Case #' + str(case) + ': ' + str(sections - 1) + '\n')
	else:
		fout.write('Case #' + str(case) + ': ' + str(sections) + '\n')
	case += 1

fin.close()
fout.close()
