f = open('A-large.in', 'rU')
lines = f.readlines()
t = int(lines[0])
out = open('A-large.out', 'a')
for i in range(1, t+1):
	n = int(lines[i])
	if n == 0: 
		out.write('Case #'+str(1)+': INSOMNIA\n')
	else:
		last_seen=n
		count_i = 1
		seen_numbers = ''
		seen_all = False
		while(not seen_all):
			last_seen = count_i*n
			for number in str(last_seen):
				if number not in seen_numbers:
					seen_numbers+=str(number)		
			if len(seen_numbers) == 10:
				seen_all = True
			else:
				seen_all = False
				count_i+=1
		out.write('\nCase #'+str(i)+': '+str(last_seen))		