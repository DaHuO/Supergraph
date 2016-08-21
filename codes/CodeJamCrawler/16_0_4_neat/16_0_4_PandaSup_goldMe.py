import itertools

def convStr(com):
	temp = []
	for i in com:
		temp.append("".join(i))
	return temp
	
def buildComplexity(combs,C,K):
	temp = []
	
	for exp in combs:
		for c in range(1,C):
			texp = ''
			for i in exp:
				if i=="L":
					texp += exp 	
				else:
					texp += "G"*K	
			temp.append(texp)
	return temp

def GCheck(com):
	temp = []
	for i in com:
		if 'G' in i:
			temp.append(True)
		else:
			temp.append(False)
	return temp	
	
def constructtrus(l, C, K):
	ret=[]
	for i in range(pow(K,C)):
		ret.append([])
	for i in range(pow(K,C)):
		for j in range(pow(2,K)):
			if l[j][i]=='G':
				ret[i]+=[True]
			else:
				ret[i]+=[False]
	return ret

def merge(l1,l2):
	l=[]
	for i in range(len(l1)):
		if l1[i] or l2[i]:
			l.append(True)
		else:
			l.append(False)
	return l

def match(l,trues):
	res=[]
	for i in range(len(l)):
		if l[i]==trues[i]:
			res.append(True)
		else:
			res.append(False)
	return res

	
def find(curr,s,i):
	temp=[]
	for j in range(i+1,pow(K,C)):
		temp=merge(curr,truthtable[j])
		if all(match(temp,Gpres)):
			return [j]
		elif s==1:
			return []
		else:
			x=find(temp,s-1,j)
			if x!=[]:
				return x+[j]
				
tc = int(input())
for i in range(1, tc+1):
	K, C, S = map(int, input().split())
	if S == 1 and K>1:
		print('Case #{}: IMPOSSIBLE'.format(i))
	elif S==K:
		temp = list(range(1,K+1))
		print('Case #{}: '.format(i), end="")
		for j in temp:
			print('{} '.format(j), end="")
		print()
	else:
		combs = list(itertools.product("LG", repeat=K))
		combs = convStr(combs)
		#print(combs)
		newComb = buildComplexity(combs,C,K)
		Gpres = GCheck(combs)
		truthtable = constructtrus(newComb,C,K)
		r=find(([False]*pow(2,K)),S,-1)
		r=[i+1 for i in r]
		f=''
		for i in r:
			f+=str(i)+' '
		print('Case #{}: {}'.format(i,str(f)))
		
		
		
