t = int(raw_input())
for z in range(t):
	x = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
	ar =''
	l = list(raw_input())
	#print(l)
	i = 0
	while(len(l) != 0):
		if('Z' in l):
			ar+='0'
		elif('W' in l):
			ar+='2'
		elif('U' in l):
			ar+='4'
		elif('X' in l):
			ar+='6'
		elif('G' in l):
			ar+='8'
		elif('V' in l):
			if('F' in l):
				ar+='5'
			else:
				ar+='7'
		elif('R' in l):
			ar+='3'
		elif('N' in l):
			if('O' in l):
				ar+='1'
			else:
				ar+='9'
		for k in x[int(ar[i])]:
				#print(l,k,x[i])
				l.remove(k)
		i+=1
		#print('---------------')
		#print(l)
	arp = list(ar)
	arp.sort()
	arpi = ''.join(arp)
	print("Case #"+str(z+1)+": "+arpi)
			
