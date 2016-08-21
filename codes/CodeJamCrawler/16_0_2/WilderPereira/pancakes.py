f = open('B-large-attempt1.in', 'rU')
lines = f.readlines()
t = int(lines[0])
out = open('b-large-attempt1.out', 'a')
x = 1
while x <= t:
	number_of_times = 0;
	pancakes = lines[x]
	if '-' not in pancakes:		
		out.write('Case #'+str(x)+': 0\n')
	elif '+' not in pancakes:
		out.write('Case #'+str(x)+': 1\n')
	else:
		not_happy = True		
		while not_happy:
			to_flip = pancakes[0]	
			if len(pancakes) > 2:
				for i in xrange(0, len(pancakes)-1):
					if pancakes[i]==pancakes[i+1] and (to_flip == '' or pancakes[i] in to_flip):
						to_flip += pancakes[i]
					else:
						break
			pancakes = pancakes.replace(to_flip,'flip',1)

			if '-' in to_flip:
				to_flip = to_flip.replace('-','+')
			else:
				to_flip = to_flip.replace('+','-')
			pancakes = pancakes.replace('flip',to_flip)
			number_of_times+=1
			if '-' not in pancakes:
				not_happy = False
			elif '+' not in pancakes:
				not_happy = False
				number_of_times+=1			
		out.write('Case #'+str(x)+': '+str(number_of_times)+'\n')
	x+=1
