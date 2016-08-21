alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
t = int(input()) 
import array
import time
for i in range(1, t + 1):
	numparties=int(input())
	S=[int (s) for s in input().split(" ")]
	G=list()
	for k in range(0,len(S)):
		G.append([S[k],k])
	#S=[S,list(range(0, len(S)))]
	S=G
	S=sorted(S)
	S.reverse()
	#print(S)
	evac=""
	curpart=0
	empty=False
	if S[curpart][0]==0:
		empty=True
	while empty==False:
		if curpart==len(S)-1:
			S[curpart][0]=S[curpart][0]-1
			evac=evac+" "+alphabet[S[curpart][1]]
			if S[curpart][0]==0:
				empty=True
		elif S[curpart][0]==S[curpart+1][0]:
			if len(S)<=2:
				S[curpart][0]=S[curpart][0]-1
				S[curpart+1][0]=S[curpart+1][0]-1
				evac=evac+" "+alphabet[S[curpart][1]]+alphabet[S[curpart+1][1]]
			elif S[curpart+2][0]==S[curpart][0]:
				S[curpart][0]=S[curpart][0]-1
			#	print(S[curpart][1])
				evac=evac+" "+alphabet[S[curpart][1]]
			else:
				S[curpart][0]=S[curpart][0]-1
				S[curpart+1][0]=S[curpart+1][0]-1
				evac=evac+" "+alphabet[S[curpart][1]]+alphabet[S[curpart+1][1]]
		else:
			S[curpart][0]=S[curpart][0]-1
			evac=evac+" "+alphabet[S[curpart][1]]
			
		#if S[curpart][0]==0:
		#	if curpart==len(S)-1:
		#		empty=True
			#else:
			#	curpart=curpart+1
		#	if S[curpart][0]==0:
			#	if curpart==len(S)-1:
			#		empty=True
				#else:
			#		curpart=curpart+1
		S=sorted(S)
		S.reverse()			
		if S[curpart][0]==0:
			empty=True
		
		#print(S)
	#	time.sleep(1)
		
	print("Case #{}: {}".format(i,evac))