import numpy as np
import os
os.system('clear')

def getAnswerMush(lines):
	n = [int(i) for i in lines[1].split(' ')]
	count = int(lines[0])
	s = 0
	for i in range(count-1):
		s+=max(n[i]-n[i+1],0)
	#second
	r = 0
	for i in range(count-1):
		if max(n[i]-n[i+1],0)>r:
			r = max(n[i]-n[i+1],0)
	sr = 0
	for i in range(count-1):
		sr+=min(n[i],r)
	return str(s)+' '+str(sr)

def gcd(*numbers):
    """Return the greatest common divisor of the given integers"""
    from fractions import gcd
    return reduce(gcd, numbers)

def lcm(*numbers):
    """Return lowest common multiple."""    
    def lcm(a, b):
        return (a * b) // gcd(a, b)
    return reduce(lcm, numbers, 1)

def getAnswerPast(lines):
	n, rank = [int(i) for i in lines[0].split(' ')]
	minutes = [int(i) for i in lines[1].split(' ')]
	m = lcm(*minutes)
	unit = 0
	for i in minutes:
		unit += m/i
	print('rank : '+str(rank))
	rank = rank%unit
	print('reduced to : '+str(rank))
	print('has '+str(n)+' workers with lcm '+str(m))
	if(rank<=n):
		print('fast')
		if(rank==0):
			return str(np.argmin(minutes)+1)
		return str(rank)
	#brute force per minute dynamics
	used = []
	#init
	for i in range(1,n+1):#numbering of hairdressers by 0, 1..
		used.append([i,minutes[i-1],minutes[i-1]])#client number and time remaining and speed
	NextClient = n+1
	while(NextClient!=rank+1):#not me sad
		#one minute
		for i in range(n):
			used[i][1]-=1
			if used[i][1]==0:
				used[i][1] = used[i][2]
				used[i][0] = NextClient
				if(NextClient==rank):#it's me!
					return str(i+1)
				NextClient += 1

def getAnswer(lines):
	r = ''
	for i in lines[0]:
		if len(r)==0 or i<r[0]:
			print(i+' last')
			r += i
		else:
			print(i+' first')
			r = i+r
	return r

def probeOne(group,name):
	lines = []
	with open(name,'r') as f: #B-small-attempt0.in.txt
		k=0
		for line in f:
			if(k>0):
				N = line
				if(N[-1]=='\n'):#treat the end lines
					N=N[:-1]
				lines.append(N)
				if len(lines) == group:#filled, send to algo
					break
			k+=1
	return lines

def getResults(group,name):#how many lines to read before using the algo
	results=[]
	with open(name,'r') as f: #B-small-attempt0.in.txt
		k=0
		lines = []
		for line in f:
			if(k>0):
				N = line
				if(N[-1]=='\n'):#treat the end lines
					N=N[:-1]
				lines.append(N)
				if len(lines) == group:#filled, send to algo
					print('***********')
					results.append(getAnswer(lines))
					print('answer : '+str(results[-1]))
					lines = []
					print('done')
				if 'str' in line:
					break
			k+=1
	return results

def writeResults(results,name):
	with open(name,'wb') as f:
		for i in range(len(results)):
			f.write("Case #"+str(i+1)+": ")
			f.write(str(results[i]))
			f.write("\n")#assumes full Case#i

# from mush import probeOne, getResults, writeResults

group = 1

#dev
lines = probeOne(group,'mock.txt')

#try the dummy
results = getResults(group,'mock.txt')
writeResults(results,'answerMock')

#try the real
fileName = 'A-small-.in.txt'
results = getResults(group,fileName)
writeResults(results,'answer'+fileName)
