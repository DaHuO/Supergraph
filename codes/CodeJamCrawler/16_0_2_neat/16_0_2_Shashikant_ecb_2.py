nt = input()
for n in range(1, nt+1):
	s = list(raw_input())
	j = 0
	k = 0
	if '+' not in s:
		k = k+1
	elif '-' not in s:
		pass
	else:
		for index,c in enumerate(s):
			if(len(s) - 1 == index):
                                break
			if s[index] != s[index+1]:
				j = 0
				while(j <= index):
					if(s[j] == '+'):
						s[j] = '-'
					else:
						s[j] = '+'
					j = j+1
				k = k+1
			if '+' not in s:
                		k = k+1
				break
        		if '-' not in s:
                		break
			#print k
	print 'Case #'+str(n)+': '+str(k)
					
	
