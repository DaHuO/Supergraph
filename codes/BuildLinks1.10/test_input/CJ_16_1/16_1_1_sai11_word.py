fin=open('A-large.in','r')
# fin=open('test.in','r')
T=int(fin.readline())

file('A-large.out','w')
f=open('A-large.out','w')


for t in xrange(T):
	S = fin.readline().strip()
	if S:
		out = S[0]
		for c in S[1:]:
			if c >= out[0]:
				out = c+out
			else:
				out += c
	else:
		out = ''
	
	f.write('Case #'+str(t+1)+': '+out+'\n')

f.close()