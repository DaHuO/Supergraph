lines = [line.rstrip('\n') for line in open('B-large.in')]

lines.remove(lines[0])
globecount = 1
# print lines

myfile = open("out2.txt",'w')

for strin in lines:
	s = []
	strin = strin[::-1]
	strin = list(strin)#[i for i in strin]
	print strin
	count = 0
	# strin1 = strin.reverse()
	# print strin1
	for charactr in strin:
		s.append(charactr)
	while '-' in s:
		i = len(s)-1
		lengt = i
		num = 0
		while (not (i < 0)) and (s[i] =='-'): 
			i = i - 1
			num = num + 1
		temparr = []
		if num > 0:
			while i <= lengt:
				s[i] = '+'
				i = i + 1
		else:
			if i < 0:
				s = ['+'] * len(s)
				# print "here"
			else:
				k = i
				while (not (k < 0)) and (s[k] =='+'):#(i+1) < len(s):
					k = k - 1
					# print "here"
				k = k + 1
				if not k == 0:
					while k <= lengt:
						temparr.append(s.pop())
						k = k + 1
						# print "here1"
					j = 0
					while j < len(temparr):
						if temparr[j] == '+':
							temparr[j] = '-'
						else:
							temparr[j] = '+'
						j=j+1
					s = s + temparr
				else:
					i = i + 1
					s = ['+']*lengt
				
		count = count+1
	# print count

	myfile.write("Case #" + str(globecount) + ": " + str(count) + "\n")
	globecount = globecount + 1
	# print len(s)


myfile.close