case_count = 1
T = input()
while(T!=0):
	count=0
	pancake = raw_input()
	length = len(pancake)
	x = '+'*length
	y = '-'*length
	if(pancake == x):
		print "Case #" + str(case_count) + ": 0"
		case_count = case_count + 1
	else:

		pan = list(pancake)
		while(True):
			cake = ''.join(pan)
			if(cake == x):
				#print "x"
				print "Case #" + str(case_count) + ": " + str(count)
				case_count = case_count + 1
				break
			if(cake == y):
				z=1
				count = count+1
				print "Case #" + str(case_count) + ": " + str(count)
				case_count = case_count + 1
				break
			q=1
			count=count+1
			pan = list(cake)
			first = pan[0]
			if(pan[0] == '+'):
				pan[0] = '-'
			else:
				pan[0] = '+'
			i=1
			while pan[i] == first:
				if(pan[i] == '+'):
					pan[i] = '-'
					i=i+1
				else:
					pan[i] = '+'
					i=i+1
	T = T-1
		
		  
