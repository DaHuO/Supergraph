def tilecopyposition(K,C,originalpos):
	if C==1:
		return originalpos
	else:
		return tilecopyposition(K,C-1,originalpos)+K**(C-1)

t = int(input()) 
for i in range(1, t + 1):
	K,C,S=[int (s) for s in input().split(" ")]
	#print(str(tilecopyposition(K,C,2)))
	if K>S or (K/2>S and C==1):
		print("Case #{}: IMPOSSIBLE".format(i))
	elif K<=S:
		tilelocations=""
		for k in range(0,K):
			tilelocations=tilelocations+" "+str(k*K**(C-1)+1)
		print("Case #{}:{}".format(i,tilelocations))
	elif S>=K/2 and C>=2:
		tilelocations=""
		for k in range(0,K//2):
			tilelocations=tilelocations+" "+str(K**(C-1)*2*k+tilecopyposition(K,C-1,2*k+2))
		if K %2>0:
			tilelocations=tilelocations+" "+str(K**(C-1)*(2*k+2)+1)
		print("Case #{}:{}".format(i,tilelocations))

	#print("Case #{}: {} {} {}".format(i,K,C,S))
			
		
	
