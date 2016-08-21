import re
import numpy as np
import itertools

f = open("in.in","r")
w = open("output.txt","w")
num = f.readline()
for it in range(0,int(num)):
	
	K,C,S = [int(l) for l in f.readline().split()]
	'''
	#This is brute force
	space = {}
	for i in range((2**K)-1):
		com = {}
		com[0] = ori = ('{0:0'+str(K)+'b}').format(i).replace('0','G').replace('1','L')
		for j in range(C-1):
			s = ''
			for k in range(K**(j+1)):
				if com[j][k]=='L':
					s+= ori
				else:
					s+= 'G' * K
			com[j+1] = s
		space[i] = com[C-1]
	listspace = [space[key] for key,v in enumerate(space)]
	searchSpace = [[ i=='L' for i in s] for s in list(map(list,zip(*listspace)))]
	
	
	#print(searchSpace)
	possibleAnswer = itertools.combinations(range(K**(C)),S)
	for i in possibleAnswer:
		#print('i',i)
		comp = [True]*(len(searchSpace[0]))
		for j in i:
			#print('j',j)
			comp = [(x and y) for x,y in zip(comp,searchSpace[j])]
		if not any(comp):
			res = ' '.join([str(a+1) for a in i])
			break
	else:
		res = 'IMPOSSIBLE'
	'''
	
	'''
	#This is small-input tricked v1
	space = {}
	for i in range((2**K)-1):
		com = {}
		com[0] = ori = ('{0:0'+str(K)+'b}').format(i).replace('0','G').replace('1','L')
		for j in range(C-1):
			s = ''
			for k in range(K**(j+1)):
				if com[j][k]=='L':
					s+= ori
				else:
					s+= 'G' * K
			com[j+1] = s
		space[i] = com[C-1]
	listspace = [space[key] for key,v in enumerate(space)]
	searchSpace = [[ i=='L' for i in s] for s in list(map(list,zip(*listspace)))]
	
	t = range(K)
	for i in range(1,C):
		t = [K*t[x]+x for x in range(K)]
	
	comp = [True]*len(searchSpace[0])
	for i in t:
		comp = [(x and y) for x,y in zip(comp,searchSpace[i])]
	if not any(comp):
		res = ' '.join([str(a+1) for a in t])
	else:
		res = 'IMPOSSIBLE'
		
	'''
	'''#this is small input tricked v2
	space = {}
	for i in range((2**K)-1):
		ori = ('{0:0'+str(K)+'b}').format(i).replace('0','G').replace('1','L')
		space[i] = ori
	listspace = [space[key] for key,v in enumerate(space)]
	searchSpace = [[ i=='L' for i in s] for s in list(map(list,zip(*listspace)))]
	'''
	t = range(K)
	for i in range(1,C):
		t = [K*t[x]+x for x in range(K)]
	res = ' '.join([str(a+1) for a in t])
	
	print("Case #{0}: {1} ".format(it+1,res))
	w.write("Case #{0}: {1}\n".format(it+1,res))
w.close()