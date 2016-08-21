import sys
from copy import copy, deepcopy
f = open(sys.argv[1], 'r')
result = open(sys.argv[1]+'.sol','w')
T=eval(f.readline())
LINE=False
COLUMN=True
def test(N, ma, b, curr, l):
	print "Testing ", N, ma,b,curr,l
	if curr>=N:
		return False
	if b:
		if curr>=1:
			if ma[0][curr-1]==0:
				return False
		for i in range(N):
			if i>=1 and ma[i-1][curr]>0 and ma[i-1][curr]>=l[i]:
				return False
			if i<=N-2 and ma[i+1][curr]>0 and ma[i+1][curr]<=l[i]:
				return False
			if curr>=1 and ma[i][curr-1]>0 and ma[i][curr-1]>=l[i]:
				return False
			if curr<=N-2 and ma[i][curr+1]>0 and ma[i][curr+1]<=l[i]:
				return False
			if ma[i][curr]>0 and ma[i][curr]!=l[i]:
				return False
		print 'success'
		return True
	else:
		if curr>=1:
			if ma[curr][0]==0:
				return False
		for i in range(N):
			if i>=1 and ma[curr][i-1]>0 and ma[curr][i-1]>=l[i]:
				return False
			if i<=N-2 and ma[curr][i+1]>0 and ma[curr][i+1]<=l[i]:
				return False
			if curr>=1 and ma[curr-1][i]>0 and ma[curr-1][i]>=l[i]:
				return False
			if curr<=N-2 and ma[curr+1][i]>0 and ma[curr+1][i]<=l[i]:
				return False
			if ma[curr][i]>0 and ma[curr][i]!=l[i]:
				return False
		print 'success'
		return True

print 'T = ', T
for t in range(T):
	tryl=[]

	print "Case #", t+1
	N=eval(f.readline())
	ls=[False for _ in range(N)]
	cs=[False for _ in range(N)]
	currl=0
	currc=0
	holel=-1
	holec=-1
	m=[[] for _ in range (2*N-1)]
	for n in range(2*N-1):
		l = tuple(map(eval,f.readline().split()))
		m[n]=l
	m.sort()
	print m
	ma=[[0]*N for _ in range(N)]
	n=0
	while n<2*N-1:
		# if currl==N-1 or currc==N-1:
		# 	break
		testL=currl<N and test(N,ma,LINE,currl,m[n])
		if testL==False and holel==-1 and currl<=N-1 and ma[currl][0]<m[n][0]:
			testL=test(N,ma,LINE,currl+1,m[n])
			if testL:
				holel=currl
				currl+=1
				
		testC=currc<N and test(N,ma,COLUMN,currc,m[n])
		if testC==False and holec==-1 and currc<=N-1 and ma[0][currc]<m[n][0]:
			testC=test(N,ma,COLUMN,currc+1,m[n])
			if testC:
				holec=currc
				currc+=1
		if testL and testC:
			print 'Two possible paths'
			print n, currl, currc, holel, holec, ma

			tryl.append((n, currl, currc, holel, holec, deepcopy(ma)))
			for j in range(N):
				ma[currl][j]=m[n][j]
			currl+=1
			print ma
			print '---------------'

		elif testL==False and testC:
			for j in range(N):
				ma[j][currc]=m[n][j]
			currc+=1
			print ma
			print '---------------'
		elif testL and testC==False:
			for j in range(N):
				ma[currl][j]=m[n][j]
			currl+=1
			print ma
			print '---------------'
		else:
			if len(tryl)==0:
				print 'breaking'
				break

			print 'Before going back'
			print ma
			print tryl
			n,currl,currc,holel,holec, ma=tryl.pop()
			print n,currl,currc,holel,holec
			print 'After going back , before changes'
			print ma
			for j in range(N):
				ma[j][currc]=m[n][j]
			currc+=1
			print 'after changes'
			print ma
			print '---------------'	
			

		n+=1
	print 'currl = ',currl
	print 'currc = ', currc
	if currl<=N-1:
		holel=N-1
	elif currc<=N-1:
		holec=N-1
	print ma
	if holec>-1:
		s=[]
		for i in range(N):
			s.append(str(ma[i][holec]))
		print 'hole is c ', holec
		result.write('Case #'+str(t+1)+': '+' '.join(s)+'\n')
	else:
		print 'hole is l ', holel
		result.write('Case #'+str(t+1)+': '+' '.join(map(str,ma[holel]))+'\n')
		# result.write('\n')

f.close()
result.close()