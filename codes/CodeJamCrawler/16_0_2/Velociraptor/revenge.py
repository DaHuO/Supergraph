# def reversereplace(strang):
# 	print 'strang ', strang
# 	newstrang = strang[::-1]
# 	print 'rev ', newstrang
# 	for c in xrange(len(newstrang)):
# 		if newstrang[c] == '-':
# 			newstrang[c]  = '+'
# 		else:
# 			newstrang[c] = '-'
# 	print 'newstrang ', newstrang
# 	return newstrang

# def cake1(ser):
# 	print 'initial ', ser
# 	count = 0
# 	end = len(ser) - 1
# 	nextMinus = 0
# 	i=0
# 	while 1:
# 		nextChar = ser[nextMinus + i]
# 		if nextChar == '-':
# 			nextMinus = nextMinus - i
# 			revv = reversereplace(ser[:nextMinus+1])
# 			print 'revv ', revv
# 			ser = revv+ser[nextMinus+1:]
# 			print 'new serr ', ser
# 			count+=1
# 			i=0
# 		i+=1
# 		if i + nextMinus > end:
# 			return count


# def cake2(ser):
# 	count = 0
# 	index = 0
# 	end = len(ser)
# 	while index < end:
# 		nextChar = ser[index]
# 		if nextChar == '-':
# 			# flip up to first -
# 			revv = reversereplace(ser[:nextMinus])
# 			print 'revv 1 ', revv
# 			ser = revv+ser[nextMinus:]
# 			print 'new serr 1 ', ser
# 			count += 1
# 			# flip at last conseq -
# 			revv = reversereplace(ser[:nextMinus+1])
# 			print 'revv 2 ', revv
# 			ser = revv+ser[nextMinus+1:]
# 			print 'new serr 2 ', ser

def cake(ser):
	# count changes and add 1 for last char -
	count = 0
	curr = ser[0]
	r = len(ser)
	for i in range(r):
		next = ser[i]
		if next != curr:
			curr = next
			count += 1
	if ser[-1] == '-':
		count += 1
	return count

inputt = open('revenge.txt','r')
outfile = open('output.txt', 'w')
totals = inputt.readline()

i = 1
for line in inputt:
	outputt = cake(list(line.strip()))
	outfile.write('Case #%s: %s\n' %(i, outputt))
	i += 1