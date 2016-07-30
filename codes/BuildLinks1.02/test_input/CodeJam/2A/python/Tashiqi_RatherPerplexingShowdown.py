T=int(input())
def coup(i):
	global R,P,S
	return("R" if i<R else ("P" if i<P+R else "S"))

def create(winner):
	global res,players
	for i in players[winner]:
		res+=[coup(i)]
		create(i)
	
def ranger(i,j):
	global res
	if j==i+2:
		res[i],res[i+1]=min(res[i],res[i+1]),max(res[i],res[i+1])
	else:
		ranger(i,(i+j)//2)
		ranger((i+j)//2,j)
		k1=i
		k2=(i+j)//2
		while res[k1]==res[k2]:
			k1+=1
			k2+=1
		if res[k1]>res[k2]:
			m=(i+j)//2
			for k in range((j-i)//2):
				res[i+k],res[m+k]=res[m+k],res[i+k]

for t in range(T):
	N,R,P,S = [int(i) for i in input().split()]
	NB = 2**N
	n,r,p,s = N,R,P,S
	next_r,next_p,next_s=r,p,s
	players=[[] for i in range(NB)]
	mort = [False for i in range(NB)]
	while r<=p+s and p<=r+s and s<=p+r and p+r+s!=1:
		it_R,it_P,it_S=0,R,R+P
		while p+r+s!=0:
			while it_R<R and mort[it_R]:
				it_R+=1
			while it_P<R+P and mort[it_P]:
				it_P+=1
			while it_S<R+P+S and mort[it_S]:
				it_S+=1
			if r<=p and r<=s:
				p-=1
				s-=1
				next_p-=1
				players[it_S]+=[it_P]
				mort[it_P]=True
				winner=it_S
				it_P+=1
				it_S+=1
			elif p<=r and p<=s:
				r-=1
				s-=1
				next_s-=1
				players[it_R]+=[it_S]
				mort[it_S]=True
				winner=it_R
				it_S+=1
				it_R+=1
			elif s<=r and s<=p:
				p-=1
				r-=1
				next_r-=1
				players[it_P]+=[it_R]
				mort[it_R]=True
				winner=it_P
				it_P+=1
				it_R+=1
		r,p,s=next_r,next_p,next_s
	if p+r+s!=1:
		print("Case #" + str(t+1) + ":", "IMPOSSIBLE")
	else:
		res = [coup(winner)]
		create(winner)
		ranger(0,NB)
		print("Case #" + str(t+1) + ":", "".join(res))