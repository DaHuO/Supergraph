T = input()
i = 1
def flipCakes(s,n):
	if(n==1):
		if(s[0] == '+'):
			return 0
		else:
			return 1
	else:
		flips = flipCakes(s,n-1)
		if(s[n-2] == '-'):
			return flips
		else:
			if(s[n-1] == '+'):
				return flips
			else:
				return flips + 2

while(T):
	s = raw_input()
	print 'Case #'+str(i)+': '+str(flipCakes(s,len(s)))
	i += 1
	T -= 1
