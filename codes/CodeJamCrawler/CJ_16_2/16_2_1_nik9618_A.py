f = open('/Users/nik9618/Downloads/A-large.in', 'r')
n = int(f.readline())
strfn = str;
c = 1
for _ in range(n):
	s = f.readline().split("\n")[0];
	
	ch = {};
	for x in s:
		if( x in ch):
			ch[x]+=1
		else:
			ch[x]=1

	num = [0,0,0,0,0,0,0,0,0,0,0]
	str = ['ZERO','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE']
	lead = ['Z','','W','','U','','X','','G','']
	solvable=[0,2,3,4,6,8,9]
	
	for s in solvable:
		if(lead[s] =='' or lead[s] not in ch):
			continue;
		numz = ch[lead[s]]
		num[s] = numz;
		for x in str[s]:
			if(x not in ch) : continue;
			ch[x]-=numz

	if('O' in ch):
		num[1] = ch['O']
		for x in str[1]:
			if(x not in ch) : continue;
			ch[x]-=num[1]

	if('H' in ch):
		num[3] = ch['H']
		for x in str[3]:
			if(x not in ch) : continue;
			ch[x]-=num[3]

	if('F' in ch):
		num[5] = ch['F']
		for x in str[5]:
			if(x not in ch) : continue;
			ch[x]-=num[5]

	if('S' in ch):
		num[7] = ch['S']
		for x in str[7]:
			if(x not in ch) : continue;
			ch[x]-=num[7]

	if('I' in ch):
		num[9] = ch['I']
		for x in str[9]:
			if(x not in ch) : continue;
			ch[x]-=num[9]

	ans = '';
	for i in range(len(num)):
		for k in range(num[i]):
			ans =  ans + strfn(i)
	print "Case #"+strfn(c)+': '+ans
	c+=1



# WEIGHFOXTOURIST
# OURNEONFOE
# ETHER