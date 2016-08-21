
tournoi_optimal_P=['']*13
tournoi_optimal_R=['']*13
tournoi_optimal_S=['']*13

tournoi_optimal_P[0]='P'
tournoi_optimal_R[0]='R'
tournoi_optimal_S[0]='S'

for k in range(1,13):
	tournoi_optimal_P[k]=min(tournoi_optimal_P[k-1]+tournoi_optimal_R[k-1],tournoi_optimal_R[k-1]+tournoi_optimal_P[k-1])
	tournoi_optimal_R[k]=min(tournoi_optimal_R[k-1]+tournoi_optimal_S[k-1],tournoi_optimal_S[k-1]+tournoi_optimal_R[k-1])
	tournoi_optimal_S[k]=min(tournoi_optimal_P[k-1]+tournoi_optimal_S[k-1],tournoi_optimal_S[k-1]+tournoi_optimal_P[k-1])

def executer_calcul(entrees):
	N=entrees[0]
	R=entrees[1]
	P=entrees[2]
	S=entrees[3]
	Case=entrees[4]
	result='z'
	if(P==tournoi_optimal_P[N].count('P') and R==tournoi_optimal_P[N].count('R') and S==tournoi_optimal_P[N].count('S')):
		result=min(result,tournoi_optimal_P[N])
	if(P==tournoi_optimal_R[N].count('P') and R==tournoi_optimal_R[N].count('R') and S==tournoi_optimal_R[N].count('S')):
		result=min(result,tournoi_optimal_R[N])
	if(P==tournoi_optimal_S[N].count('P') and R==tournoi_optimal_S[N].count('R') and S==tournoi_optimal_S[N].count('S')):
		result=min(result,tournoi_optimal_S[N])
	if(result=='z'): return 'IMPOSSIBLE'
	return result

def executer_gagnant(N,s):
	if(N==0): return s
	if(N==1 and s=='P'): return 'PR'
	if(N==1 and s=='R'): return 'RS'
	if(N==1 and s=='S'): return 'PS'
	rang_precedent=executer_gagnant(N-1,s)
	accu=''
	for i in range(len(rang_precedent)):
		accu=accu+executer_gagnant(1,rang_precedent[i])
	return accu

# Main
multiprocessed=False # Décide si l'on parallélise les calculs pour gagner du temps
if (multiprocessed): from multiprocessing import Pool
else: output = open('Output.txt','w')
if ((not multiprocessed) or __name__ == '__main__'):
	with open("Input.txt", "r") as input:
		lines=input.readlines()
	T=int(lines[0])
	line=1
	Case=1
	calculs=[]
	while(line<len(lines)):
		N,R,P,S=map(int,lines[line].split(' '))
		line=line+1
		entrees=[N,R,P,S,Case]
		if (not multiprocessed): output.write('Case #'+str(Case)+': '+executer_calcul(entrees)+'\n')
		else: calculs.append(entrees)
		Case=Case+1
	if (multiprocessed):
		pool=Pool(3) # Décide du nombre de processus à faire tourner en parallèle
		results=pool.map(executer_calcul,calculs)
		output = open('Output.txt','w')
		for case in range(len(results)):
			output.write('Case #'+str(case+1)+': '+results[case]+'\n')
	output.close()

