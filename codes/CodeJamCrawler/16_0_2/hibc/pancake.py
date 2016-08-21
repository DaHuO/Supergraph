f = open ('B-large.in.txt','r')
fw = open ('output.txt','w')
test_case = int(f.readline())

#test_case = int (raw_input())  # remove

for i in range(0, test_case):
	lst = []
	cake = str(f.readline())
	cake = cake.rstrip('\n')
	#cake = raw_input()
	lst = map(str,cake)
	#print lst

	#print i
	#print lst
	if (len(lst) == 1):
		#print 'sup'
		if (lst[0] == '-'):
			print >> fw , 'Case #%d: %d' % (i+1, 1)
		else:
			print >> fw , 'Case #%d: %d' % (i+1, 0)
	elif ( len(set(lst)) == 1):
		if (lst[0] == '-'):
			print >> fw , 'Case #%d: %d' % (i+1, 1)
		else:
			print >> fw, 'Case #%d: %d' % (i+1, 0)
	else:	
		j = 0
		cnt = 0
		flip = 0

		while (1):
			
			if ( (j+1) <= len(lst)):
				if ( lst[j] != lst[j+1]):
					lst[0:cnt] = lst[j+1] * (cnt)
					lst[j] = lst[j+1]
					flip = flip + 1
					#print lst
					if ( len(set(lst)) == 1):
						if (lst[0] == '+'):
							#print 'aa'
							break
						else:
							#print 'bb'
							flip  = flip + 1
							break
					else:
						j = 0
						cnt = 0
						continue
				else:
					cnt = cnt + 1
					j = j+1

		print >>fw,'Case #%d: %d' % (i+1, flip) 

f.close()
fw.close()