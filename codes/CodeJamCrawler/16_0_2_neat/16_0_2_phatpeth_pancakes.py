T = int(input())
ans = ""
for i in range(T):
	S = input()
	count = 0
	if '-' not in S:
		ans += ("Case #"+str(i+1)+": 0\n")
	else:
		#for c in S[::-1]:
		for p in range(len(S))[::-1]:
			#if c == '-':
			#	print(S[::-1] + S[:])
			if S[p] == '-':
				count += 1
				SS = S[:p+1].replace('-','m')
				SS = SS.replace('+','-')
				S = SS.replace('m','+') + S[p+1:]
			#print(S);
		ans += ("Case #"+str(i+1)+": "+str(count)+"\n")

print(ans)
#ans += ("Case #"+str(i+1)+": "+str(N*T)+"\n")