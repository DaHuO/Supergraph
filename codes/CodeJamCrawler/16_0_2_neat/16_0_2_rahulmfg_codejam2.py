#! usr/bin/python

# 1 (--++)
# 2 (-+-+-)
# 3 (+++---)
# 4 (++-+-)
f = open("B-large.in")

noc = int(f.readline())
case = 1

def patternId(cakes):
	if cakes[0] == '-':
		j = 1
		noMAP = True
		foundP = False
		while j < len(cakes):
			if cakes[j] == '+':
				foundP = True
			elif foundP and cakes[j] == '-': 
				noMAP = False
				break
			j += 1
		if noMAP:
			return 1
		else:
			return 2
	else:
		j = 1
		noPAM = True
		foundM = False
		while j < len(cakes):
			if cakes[j] == '-':
				foundM = True
			elif foundM and cakes[j] == '+':
				noPAM = False
				break
			j += 1
		if noPAM:
			return 3
		else:
			return 4

if noc <= 100:
	for line in f:
		pancakes = line
		noS = 0
		while '-' in list(pancakes):
			if '+' not in list(pancakes):
				noS += 1
				break
			else:	
				key = patternId(pancakes)
				
				#case 1
				if key == 1:
					#print "Doing 1 for %s" % pancakes
					keyI = 0
					for index, c in enumerate(list(pancakes)):
						if c == '+':
							keyI = index
							break
					pancakes = (pancakes[:keyI].replace('-','+'))[::-1] + pancakes[keyI:]
					#print 'New %s ' % pancakes
					noS += 1
				#case 2
				elif key == 2:
					tmp = list(pancakes)
					i = len(tmp) - 1
					keyI = 0
					while i >= 0:
						if tmp[i] == '-':
							keyI = i
							break
						i -= 1
					i = 0
					tstr = ''
					while i <= keyI:
						if tmp[i] == '+':
							tstr += '-'
						else:
							tstr += '+'
						i += 1
					pancakes = tstr[::-1] + pancakes[keyI + 1:]
					noS += 1
				# case 3 or 4
				elif key == 3 or key == 4:
					keyI = 0
					for index, c in enumerate(list(pancakes)):
						if c == '-':
							keyI = index
							break
					pancakes = (pancakes[:keyI].replace('+','-'))[::-1] + pancakes[keyI:]
					noS += 1
		print 'Case #%d: %d' % (case, noS)
		noS = 0
		case += 1

