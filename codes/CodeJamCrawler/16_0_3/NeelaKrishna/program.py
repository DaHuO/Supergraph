

def digitize(N):
	digits=[]
	for i in list(str(N)):
		i=int(i)
		if i not in digits:
			digits.append(i)
	return digits

def flip():
	pass

from collections import Counter
from itertools import groupby

def consecutivetopscenario(group):
	print group
	side=0
	for i,v in enumerate(group[::-1]):
		print i,v
		if group[-1] == v:
			side=side+1
		else:
			break
	counterside=0
	print group[:-1*(i)]
	for j,v in enumerate(group[:-1*(i)][::-1]):
		print j,v
		if group[-1] != v:
			counterside=counterside+1
		else:
			break
	return {group[-1]:side,group[-1*(i+1)]:counterside}

from itertools import permutations,product

def doit(N,J):
	output="\n"
	for permutation in list(product(['0','1'],repeat=(N-16)))[::-1]:
		coin="".join(['1','1','1','1','1','1','1','1']+list(permutation)+['1','1','1','1','1','1','1','1'])
		nontrivialdivisors=[]
		for base in range(2,11):
			number=int(coin,base)
			# print coin,str(base),str(number)
			for j in range(2,10000):
				if number%j == 0:
					nontrivialdivisors.append(j)
					break
		if J>0:
			if len(nontrivialdivisors) == 9:
				J=J-1
				output=output+coin+" "+" ".join(map(str,nontrivialdivisors))+"\n"
			print output
		else:
			break
	return output





	# if results['+'] > results['-'] and group[-1]=='-':
		# flip(group)

	# print Counter(pancakes)




fo=open("output.out","w")
f=open("C-large.in","r")
inp=f.read()
print inp
f.close()
inp=inp.split('\n')
T=int(inp[0])
inp=inp[1:]
for x in range(T):
	fo.write("Case #"+str(x+1)+": "+str(doit(*map(int,inp[x].split(" "))))+"\n")
fo.close()