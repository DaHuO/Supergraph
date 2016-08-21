t = int(input())

for T in range(1, t+1):
	s = input()
	N = 1
	if(int(s) == 0):
		print("CASE #"+str(T)+": INSOMNIA")
	else:
		check_set = {'0','1','2','3','4','5','6','7','8','9'}
		ss = set([i for i in s])
		while(check_set != ss):
			ss = ss.union(set([i for i in str(int(s)*N)]))
			#print(ss, N, int(s)*N)
			N = N + 1
		print("CASE #"+str(T)+": "+str((N-1)*int(s)))
