import sys



n = int(input())

for i in range(n):
	strline = raw_input()

	stacklist = []
	for c in strline:
		stacklist.append(c)

	# print(stacklist)

	count = 0

	l = len(stacklist)

	if l == 1:
		if stacklist[0] == '-':
			count = 1
	elif l > 1:
		for j in range(l-1):
			if stacklist[j] != stacklist[j+1]:
				count += 1
		if stacklist[l-1] == '-':
			count += 1

	strA = 'Case #%d: '%(i+1)
	strB = '%d' %(count)

	printstr = strA + strB
	print(printstr)
