from collections import Counter
filename = "A-large"
infile= filename + '.in'
f = open(infile)
inp = f.readlines()
f.close()
outfile = filename + '.out'
f = open(outfile,'w')
case = int(inp.pop(0))
for case in range(1, case + 1):
	Str = inp.pop(0).strip()
	phone = list()
	cnt = Counter(Str)
	while any(cnt[item] > 0 for item in cnt):
		if cnt['Z']:
			while(cnt['Z']):
				phone.append('0')
				cnt['Z'] -= 1
				cnt['E'] -= 1
				cnt['R'] -= 1
				cnt['O'] -= 1
		if cnt['W']:
			while(cnt['W']):
				phone.append('2')
				cnt['T'] -= 1
				cnt['W'] -= 1
				cnt['O'] -= 1
		if cnt['U']:
			while(cnt['U']):
				phone.append('4')
				cnt['F'] -= 1
				cnt['O'] -= 1
				cnt['U'] -= 1
				cnt['R'] -= 1
		if cnt['X']:
			while(cnt['X']):
				phone.append('6')
				cnt['S'] -= 1
				cnt['I'] -= 1
				cnt['X'] -= 1
		if cnt['G']:
			while(cnt['G']):
				phone.append('8')
				cnt['E'] -= 1
				cnt['I'] -= 1
				cnt['G'] -= 1
				cnt['H'] -= 1
				cnt['T'] -= 1
		if cnt['R']:
			while(cnt['R']):
				phone.append('3')
				cnt['T'] -= 1
				cnt['H'] -= 1
				cnt['R'] -= 1
				cnt['E'] -= 2	
		if cnt['F']:
			while(cnt['F']):
				phone.append('5')
				cnt['F'] -= 1
				cnt['I'] -= 1
				cnt['V'] -= 1
				cnt['E'] -= 1
		if cnt['V']:
			while(cnt['V']):
				phone.append('7')
				cnt['S'] -= 1
				cnt['E'] -= 2
				cnt['V'] -= 1
				cnt['N'] -= 1
		if cnt['I']:
			while(cnt['I']):
				phone.append('9')
				cnt['N'] -= 2
				cnt['I'] -= 1
				cnt['E'] -= 1				
		if cnt['O']:
			while(cnt['O']):
				phone.append('1')
				cnt['O'] -= 1
				cnt['N'] -= 1
				cnt['E'] -= 1
							

	phone = sorted(phone)
	result = "".join(phone)
	print('Case #{}: {}'.format(case, result))
	f.write('Case #{}: {}\n'.format(case, result))
f.close()	
