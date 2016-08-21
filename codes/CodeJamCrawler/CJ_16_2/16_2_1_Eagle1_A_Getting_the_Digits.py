T=int(input())
for t in range(T):
	S=raw_input()
	N=[]
	while 'Z' in S:
		N.append('0')
		i=S.index('Z')
		S=S[:i]+S[i+1:]
		i=S.index('E')
		S=S[:i]+S[i+1:]
		i=S.index('R')
		S=S[:i]+S[i+1:]
		i=S.index('O')
		S=S[:i]+S[i+1:]
	while 'X' in S:
		N.append('6')
		i=S.index('S')
		S=S[:i]+S[i+1:]
		i=S.index('I')
		S=S[:i]+S[i+1:]
		i=S.index('X')
		S=S[:i]+S[i+1:]
	while 'G' in S:
		N.append('8')
		i=S.index('E')
		S=S[:i]+S[i+1:]
		i=S.index('I')
		S=S[:i]+S[i+1:]
		i=S.index('G')
		S=S[:i]+S[i+1:]
		i=S.index('H')
		S=S[:i]+S[i+1:]
		i=S.index('T')
		S=S[:i]+S[i+1:]
	while 'W' in S:
		N.append('2')
		i=S.index('T')
		S=S[:i]+S[i+1:]
		i=S.index('W')
		S=S[:i]+S[i+1:]
		i=S.index('O')
		S=S[:i]+S[i+1:]
	while 'U' in S:
		N.append('4')
		i=S.index('F')
		S=S[:i]+S[i+1:]
		i=S.index('O')
		S=S[:i]+S[i+1:]
		i=S.index('U')
		S=S[:i]+S[i+1:]
		i=S.index('R')
		S=S[:i]+S[i+1:]
	while 'F' in S:
		N.append('5')
		i=S.index('F')
		S=S[:i]+S[i+1:]
		i=S.index('I')
		S=S[:i]+S[i+1:]
		i=S.index('V')
		S=S[:i]+S[i+1:]
		i=S.index('E')
		S=S[:i]+S[i+1:]
	while 'V' in S:
		N.append('7')
		i=S.index('S')
		S=S[:i]+S[i+1:]
		i=S.index('E')
		S=S[:i]+S[i+1:]
		i=S.index('V')
		S=S[:i]+S[i+1:]
		i=S.index('E')
		S=S[:i]+S[i+1:]
		i=S.index('N')
		S=S[:i]+S[i+1:]
	while 'T' in S:
		N.append('3')
		i=S.index('T')
		S=S[:i]+S[i+1:]
		i=S.index('H')
		S=S[:i]+S[i+1:]
		i=S.index('R')
		S=S[:i]+S[i+1:]
		i=S.index('E')
		S=S[:i]+S[i+1:]
		i=S.index('E')
		S=S[:i]+S[i+1:]
	while 'O' in S:
		N.append('1')
		i=S.index('O')
		S=S[:i]+S[i+1:]
		i=S.index('N')
		S=S[:i]+S[i+1:]
		i=S.index('E')
		S=S[:i]+S[i+1:]
	while 'N' in S:
		N.append('9')
		i=S.index('N')
		S=S[:i]+S[i+1:]
		i=S.index('I')
		S=S[:i]+S[i+1:]
		i=S.index('N')
		S=S[:i]+S[i+1:]
		i=S.index('E')
		S=S[:i]+S[i+1:]
	N.sort()
	s=""
	for n in N:
		s=s+n
	print("Case #%d: %s"%(t+1,s))
