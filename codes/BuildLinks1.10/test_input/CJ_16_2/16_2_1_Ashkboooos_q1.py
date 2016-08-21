file_n = 'A-large1.in'
content = open(file_n , 'r').read().splitlines()
T, output   = int(content[0]), ''
nums = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
ones = {'Z':0,'U':4,'G':8,'W':2,'X':6}
seconds = {'F': 5, 'V':7, 'I': 9, 'H':3, 'O':1}
seconds = [ ['F', 5] ,['V',7],[ 'I', 9],[ 'H',3] ,['O',1]]
for i in xrange(1, T + 1):
	#K, C, S =  map(int, content[i].split())
	s = content[i].strip()
	#print 's ' ,s
	case = "Case #%d: " %i 
	found = []
	for key in ones:
		flag= True
		while flag:
			if key in s:
				#print key
				found.append(ones[key])
				for e in nums[ones[key]]:
					s = s.replace(e,'',1)
				#print s
			else:
				flag = False
	for key in seconds:
		#print '1.5 ', key
		flag= True
		while flag:
			if key[0] in s:
				#print '2  ', key
				found.append(key[1])
				for e in nums[key[1]]:
					s = s.replace(e,'',1)	
				#print s
			else:
				flag = False
	assert s == ''
	case += ''.join(map(str,sorted(found)))		
	output += case + '\n'
file_out = file_n.replace('.in','.out')
f = open(file_out, 'w')
f.write(output)
f.close()


