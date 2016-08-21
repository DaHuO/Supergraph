import itertools

def flip(m):
	min_dict = dict()
	for string in itertools.imap(''.join, itertools.product('+-', repeat=len(m))):
		min_dict[string] = None
	min_dict['+'*len(m)] = 0
	modified = True
	count = 0
	last_modified = ['+'*len(m)]
	while modified:
		if min_dict[m] != None:
			return min_dict[m]
		count += 1
		#print 'Round ' + str(count)
		#print min_dict
		#print last_modified
		temp_list = list()
		modified = False
		for string in last_modified:
			for i in range(1,len(m)+1):
				temp_string = ''
				for j in range(i):
					if string[i-1-j] == '+':
						temp_string += '-'
					else:
						temp_string += '+'
				temp_string += string[i:]
				#print string, temp_string
				if min_dict[temp_string] == None:
					temp_list.append(temp_string)
					min_dict[temp_string] = count
					#print string, temp_string, count
					modified = True
		last_modified = temp_list
	return min_dict[m]

t = int(raw_input())  
for i in xrange(1, t + 1):
	m = raw_input()
	print "Case #{}: {}".format(i, flip(m))