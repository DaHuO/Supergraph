test=int(raw_input())

for i in range(test):
	inp=raw_input()
	t='-'
	if '-' not in inp:
		print "Case #"+str(i+1)+": "+str(0)
	else:
		k=0
		while '-' in inp:
			if '+' not in inp:
				k+=1
				break
			ind=inp.index(t)
			if ind==0:
				if t=='-' and '+' in inp:
					t='+'
				elif t=='+' and '-' in inp:
					t='-'
				ind=inp.index(t)
			new = ""
			for j in range(ind):
				new += t
			inp=new+inp[ind:]
			k+=1
			if t=='-' and '+' in inp:
				t='+'
			elif t=='+' and '-' in inp:
				t='-'
			elif '+' not in inp:
				k+=1
				break
		print "Case #"+str(i+1)+": "+str(k)


