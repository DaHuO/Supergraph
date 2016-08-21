#usr/bin/python
from __future__ import division
import sys

fin = open(sys.argv[1], "r")
fout = open("A.out", "w")

     

T = int(fin.readline())
for ii in xrange(T):
	q = (fin.readline().rstrip())
	teststring = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	listcount = []
	for i in range(len(teststring)):
		let = teststring[i]
		listcount.append(q.count(let))
	print listcount	
	#print teststring[17]
	#print sum(listcount)
	sol = []
	#wile sum(listcount) > 0:
	if 1:
		word = "ZERO"
		indlist = []
		print listcount[17]	
		for k in range(len(word)):
			indlist.append(teststring.index(word[k]))
		#print indlist
		ct = 	listcount[indlist[0]]
		if ct > 0:
			sol = sol + [0]*listcount[indlist[0]]
			for k in range(len(word)):
				listcount[indlist[k]] = listcount[indlist[k]] - ct
		#print listcount[17]			

		word = 'TWO'
		indlist = []
		for k in range(len(word)):
			indlist.append(teststring.index(word[k]))
		ct = 	listcount[indlist[1]]	
		if listcount[indlist[1]] > 0:
			sol = sol + [2]*listcount[indlist[1]]
			for k in range(len(word)):
				listcount[indlist[k]] = listcount[indlist[k]] - ct

		word = 'FOUR'
		indlist = []
		for k in range(len(word)):
			indlist.append(teststring.index(word[k]))
		ct = 	listcount[indlist[2]]	
		if listcount[indlist[2]] > 0:
			sol = sol + [4]*listcount[indlist[2]]
			for k in range(len(word)):
				listcount[indlist[k]] = listcount[indlist[k]] - ct		


		word = 'THREE'
		indlist = []
		for k in range(len(word)):
			indlist.append(teststring.index(word[k]))
		#print listcount[indlist[2]]	
		ct = 	listcount[indlist[2]]
		if listcount[indlist[2]] > 0:
			sol = sol + [3]*listcount[indlist[2]]
			for k in range(len(word)):
				listcount[indlist[k]] = listcount[indlist[k]] - ct

		

		word = 'SIX'
		indlist = []
		for k in range(len(word)):
			indlist.append(teststring.index(word[k]))
		ct = 	listcount[indlist[2]]	
		if listcount[indlist[2]] > 0:
			sol = sol + [6]*listcount[indlist[2]]
			for k in range(len(word)):
				listcount[indlist[k]] = listcount[indlist[k]] - ct

		word = 'EIGHT'
		indlist = []
		for k in range(len(word)):
			indlist.append(teststring.index(word[k]))
		ct = 	listcount[indlist[3]]	
		if listcount[indlist[3]] > 0:
			sol = sol + [8]*listcount[indlist[3]]
			for k in range(len(word)):
				listcount[indlist[k]] = listcount[indlist[k]] - ct

		word = 'FIVE'
		indlist = []
		for k in range(len(word)):
			indlist.append(teststring.index(word[k]))
		ct = 	listcount[indlist[0]]	
		if listcount[indlist[0]] > 0:
			sol = sol + [5]*listcount[indlist[0]]
			for k in range(len(word)):
				listcount[indlist[k]] = listcount[indlist[k]] - ct

		word = 'SEVEN'
		indlist = []
		for k in range(len(word)):
			indlist.append(teststring.index(word[k]))
		ct = 	listcount[indlist[2]]	
		if listcount[indlist[2]] > 0:
			sol = sol + [7]*listcount[indlist[2]]
			for k in range(len(word)):
				listcount[indlist[k]] = listcount[indlist[k]] - ct

		word = 'ONE'
		indlist = []
		for k in range(len(word)):
			indlist.append(teststring.index(word[k]))
		ct = 	listcount[indlist[0]]
		if listcount[indlist[0]] > 0:
			sol = sol + [1]*listcount[indlist[0]]
			for k in range(len(word)):
				listcount[indlist[k]] = listcount[indlist[k]] - ct

		word = 'NINE'
		indlist = []
		for k in range(len(word)):
			indlist.append(teststring.index(word[k]))
		ct = 	listcount[indlist[1]]	
		if listcount[indlist[1]] > 0:
			sol = sol + [9]*listcount[indlist[1]]
			for k in range(len(word)):
				listcount[indlist[k]] = listcount[indlist[k]] - ct	

	sol.sort()			
	print ''.join(map(str,sol))		


	fout.write("Case #" + str(ii+1) + ": " + ''.join(map(str,sol)) + "\n")