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

def getAnswer1(lines):
	r = ''
	for i in lines[0]:
		if len(r)==0 or i<r[0]:
			print(i+' last')
			r += i
		else:
			print(i+' first')
			r = i+r
	return r

def getAnswer2(lines):
	N=int(lines[0])
	lists = []
	for i in lines[1:]:
		n = [int(j) for j in i.split(' ')]
		lists.append(n)

	m = np.array(lists,dtype=np.int64)
	ordered = []
	remain = range(len(lists))
	for i in range(N):
		candidates = [lists[j][i] for j in remain]
		diag = min(candidates)
		index = []
		for ind,value in zip(remain,candidates):
			if value==diag:
				index.append(ind)
		ordered.append([lists[m] for m in index])
		print(len(remain))
		for m in range(len(remain))[::-1]:
			if remain[m] in index:
				del remain[m]

	matrix = np.zeros((N,N),dtype=np.int64)
	for i in range(N):
		candidates = ordered[i]
		if i==0:
			matrix[i]=candidates[0]
			if len(candidates)>1:
				matrix[:,i]=candidates[1]
		#easy
		if len(candidates)>1:
			inverse = False
			if np.sum(np.array(candidates[0][:i],dtype=np.int64)==matrix[i,:i])!=i:
				inverse = True
				matrix[:,i]=candidates[0]
				matrix[i]=candidates[1]
			if np.sum(np.array(candidates[0][:i],dtype=np.int64)==matrix[:i,i])!=i:
				inverse = True
				matrix[:,i]=candidates[1]
				matrix[i]=candidates[0]
		#normal
		matrix[i]=candidates[0]
		#test
		for j in range(i,N):
			matrix[:i+1,j] in m[:,:i+1]


def getAnswer(lines):
	answer = np.zeros(10)
	nb = ['ZERO','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE']
	order = [('ZERO','Z',0),('TWO','W',2),('FOUR','U',4),('SIX','X',6),('EIGHT','G',8),('FIVE','F',5),('THREE','R',3),('ONE','O',1),('SEVEN','V',7),('NINE','I',9)]
	letters = {letter for number in nb for letter in number}
	dic = {letter:0 for letter in letters}
	phone = lines[0]
	for letter in phone:
		dic[letter] += 1
	for number,lead,i in order:
		#retirer un nombre
		times = dic[lead]
		answer[i] = times
		for t in range(times):
			for letter in number:
				dic[letter] += -1
			# if(min(dic.values())<0):#bad
			# 	for letter in number:
			# 		dic[letter] += 1
			# 	ok = False
			# else:
			# 	answer+=str(i)
	print('max remaining : ')
	print(max(dic.values()))
	if(max(dic.values())):
		print('ERRRRRRRRRROOOOOOOOOOORRRR')
	strAnswer = ''
	for i,times in enumerate(answer):
		strAnswer += str(i)*int(times)
	return strAnswer

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

def getResultsAlt(name,algo):#how many lines to read before using the algo
	results=[]
	with open(name,'r') as f: #B-small-attempt0.in.txt
		k=0
		new=True
		number=0
		lines = []
		for line in f:
			if(k>0):
				N = line
				if(N[-1]=='\n'):#treat the end lines
					N=N[:-1]
				if new:
					number = 2*int(N)
					#print('number '+str(number))
					new = False
				else:
					number += -1
				lines.append(N)
				if number == 0:#filled, send to algo
					print('***********')
					print('sent')
					print(lines)
					results.append(algo(lines))
					print('answer : '+str(results[-1]))
					lines = []
					print('done')
					new = True
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
fileName = 'A-large.in.txt'
results = getResults(group,fileName)
writeResults(results,'answer'+fileName)
