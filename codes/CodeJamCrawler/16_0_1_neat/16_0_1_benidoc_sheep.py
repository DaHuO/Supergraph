#! python
def countSheep(num):
	if num == 0:
		return 'INSOMNIA'
	nums_seen = []
	iteration = 2
	new_dig = 1
	numstr = str(num)
	while len(nums_seen) < 10:
		#print('Seen: ', nums_seen[0:])
		#print('numstr: ' + numstr)
		for digit in numstr:
			for seen_dig in nums_seen:
				if seen_dig == digit:
					new_dig = 0
					break
			if new_dig == 1:
				nums_seen.append(digit)
			new_dig = 1
		newnum = num * iteration
		numstr = str(newnum)
		iteration += 1
	newnum = num * (iteration - 2)
	numstr = str(newnum)
	#print('return ' + numstr)
	return numstr

fin = open('A-large.in')
fout = open('large_output.txt', 'w+')
cases = int(fin.readline())
i = 1
for c in range(0, cases):
	start = int(fin.readline())
	fout.write('Case #' + str(i) + ': ' + str(countSheep(start)) + '\n')
	i += 1
fin.close()
fout.close()