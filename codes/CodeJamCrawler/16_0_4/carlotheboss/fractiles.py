pot = []

def Vai(num, liv, C, K):
	if liv==C-1: return num
	return pot[C-1-liv] *(num-1) + Vai(num, liv+1, C, K)

for i in range(int(input())):
	K,C,S = input().split()
	K,C,S = int(K), int(C), int(S)
	
	pot.clear()
	pot.append(1)
	for j in range(1, 101):
		pot.append(K*pot[j-1])
	
	if C==1 and S<K: print("Case #%s: IMPOSSIBLE" %(i+1))
	elif C==1 and S==K: print("Case #%s: %s" %(i+1, " ".join([str(i) for i in range(1,K+1)])))
	else:
		v=[]
		n=1
		while 2*n-1 <= K:
			sx = 2*n if 2*n <= K else 2*n-1
			dx = 2*n - 1
			v.append([sx, dx])
			n+=1
		
		if len(v) > S: print("Case #%s: IMPOSSIBLE" %(i+1))
		else:
			s="Case #"+str(i+1) + ": "
			for j in v:
				num = j[1]
				quale = j[0]
				ind = Vai(num, 0, C, K)
				if quale > num: ind+=1
				#print("\tVado in %s dal %s -> %s" %(quale, num, ind))
				s +=str(ind) + " "
			print(s)
