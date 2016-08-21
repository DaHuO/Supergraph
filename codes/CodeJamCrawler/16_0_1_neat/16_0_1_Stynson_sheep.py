

def countSheeps(N):
	if N == 0: return 'INSOMNIA'
	M = N
	digits = [0]*10 
	count = 0
	while count != 10:
		for j in str(M):
			if digits[int(j)] == 0:
				digits[int(j)] = 1
				count+=1 
		M += N
	return M-N


with open("input.txt") as f:
	f.readline()
	i = 1
	with open("output.txt","w") as g:
		for n in f:
			g.write("Case #"+str(i)+": "+str(countSheeps(int(n)))+"\n")
			i += 1


