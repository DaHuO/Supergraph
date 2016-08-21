from sys import argv, stdout
import operator

f = open(argv[1])
line = f.readline()
t = int(line)
c = 1
while t > 0:
	line = f.readline()
	np = int(line)
	line = f.readline().split(' ')
	np_list = []
	all = 0
	for i in xrange(len(line)):
		np_list.append(int(line[i]))
	#	all += int(line[i])
	#sort_list = sorted(np_list.items(), key=operator.itemgetter(1), reverse=True)
	stdout.write('Case #%d:' % c)
	#for i in xrange(len(sort_list)):
	#	if i < len(sort_list) - 2:
	#		if 
	while sum(np_list) > 0:
		if np_list.count(0) == np - 2:
			idx = np_list.index(max(np_list))
			np_list[idx] -= 1
			ans = chr(ord('A') + idx)
			idx = np_list.index(max(np_list))
			np_list[idx] -= 1
			ans += chr(ord('A') + idx)
			stdout.write(' %s' % ans)
			if sum(np_list) == 0:
				stdout.write('\n')
				break
		elif sum(np_list) > 2:
			idx = np_list.index(max(np_list))
			np_list[idx] -= 1
			stdout.write(' %s' % chr(ord('A') + idx))
		else:
			idx = np_list.index(max(np_list))
			np_list[idx] -= 1
			ans = chr(ord('A') + idx)
			idx = np_list.index(max(np_list))
			np_list[idx] -= 1
			ans += chr(ord('A') + idx)
			stdout.write(' %s\n' % ans)
	t -= 1
	c += 1
