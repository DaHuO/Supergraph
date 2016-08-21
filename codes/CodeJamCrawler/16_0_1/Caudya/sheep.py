def boucle(n):
	tab = [0]*10
	i = 1
	if n==0 :
		return("INSOMNIA")
	while sum(tab)!=10:
		a = int(n)*i
		for l in str(a):
			if tab[int(l)]==0 :
				tab[int(l)] = 1
		i = i+1
	return((i-1)*n)

f = open('A-large.in', 'r')
f2 = open('A-large.out', 'w')

b = f.readline()
for i in range(0,int(b)):
	f2.write("Case #"+str(i+1)+": "+str(boucle(int(f.readline())))+"\n")




