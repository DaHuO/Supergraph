from collections import Counter
for _ in range(int(input())):
	string=input()
	d={'0':4,'1':3,'2':3,'3':5,'4':4,'5':4,'6':3,'7':5,'8':5,'9':4}
	count, n_one, n_sev, v_sev, tcount_eight, tcount_two, s_six, s = 0,0,0,0,0,0,0,""
	t_three, s_sev= 0, 0
	o_zer, o_two, o_four, v_five, n_one , o_one, n_nine= 0,0,0,0,0,0,0
	for char in string:
		if count<=len(string):
			if char=='Z':
				s+='0'
				o_zer+=1
				count+=d['0']
			if char=='W':
				s+='2'
				o_two+=1
				tcount_two+=1
				count+=d['2']
			if char=='U':
				s+='4'
				o_four+=1
				count+=d['4']
			if char=='X':
				s+='6'
				s_six+=1
				count+=d['6']
			if char=='G':
				s+='8'
				tcount_eight+=1
				count+=d['8']
		else:
			break
	c=Counter(string)
	while (True):
		if count>=len(string):
			break
		elif c['T']>tcount_eight+tcount_two+t_three:
			s+='3'
			t_three+=1
			count+=d['3']
		elif c['S']>s_six+s_sev:
			n_sev+=1
			v_sev+=1
			s_sev+=1
			s+='7'
			count+=d['7']
		elif c['V']>v_sev+v_five:
			s+='5'
			v_five+=1
			count+=d['5']
		elif c['O']>o_zer+o_four+o_two+o_one:
			s+='1'
			n_one+=1
			o_one+=1
			count+=d['1']
		elif c['N']>n_sev+n_one+n_nine:
			s+='9'
			n_nine+=1
			count+=d['9']
	s=sorted(s)		
	print ("Case #{}: ".format(_+1),end="")
	print (*s,sep="")