def qq(l):
	T = ["A","B","C"]
	a = ""
	while sum(l)!=0:
		i = 0
		while l[i]!=max(l):
			i += 1
		l[i] += -1
		j = 0
		if l[i]!=0:
			while j<len(l) and l[j]<=((sum(l)-1)/2):
				j += 1
			if j>=len(l):
				a += T[i] + T[i] + " "
				l[i] += -1
			else:
				if l[j]>(sum(l)-1)/2 and l[j]>(sum(l))/2:
					a += T[i] + T[j] + " "
					l[j] += -1
				else:
					if l[j]>(sum(l)-1)/2:
						a += T[i]+" "
					
		else:
			while j<len(l) and l[j]<=(sum(l))/2:
				j += 1
			if j>=len(l):
				a += T[i]+" "
			else:
				if l[j]>(sum(l))/2:
					a += T[i]+ T[j]+" "
					l[j] += -1
	return(a)

f=open("A-small-attempt2.in", 'r')
f2=open("A-small-attempt2.out", 'w')
b=f.readline()

for k in range(int(b)):
	a = f.readline()
	c = f.readline()
	l = [int(i) for i in c.split()]		
	f2.write("Case #"+str(k+1)+": "+qq(l)+'\n')
