#usr/bin/python
from __future__ import division
import sys

fin = open(sys.argv[1], "r")
fout = open("A.out", "w")
     

T = int(fin.readline())
for ii in xrange(T):
	tot = int(fin.readline())
	mem_counts =  map(lambda x: int(x),fin.readline().split())
	#print mem_counts
	max_count = max(mem_counts)
	max_pos = [i for i, j in enumerate(mem_counts) if j == max_count]
	lets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	print mem_counts, max_pos, len(lets)
	sol = []
	if len(max_pos) == 1:
		print 'here'
		temp_counts = mem_counts[:]
		temp_counts[max_pos[0]] = 0
		max_count_temp = max(temp_counts)
		max_pos_temp = temp_counts.index(max_count_temp)
		len_elim = max_count - max_count_temp
		print len_elim
		for j in range(len_elim//2):
			sol.append(lets[max_pos[0]]+lets[max_pos[0]])
		if len_elim%2 == 1:
			sol.append(lets[max_pos[0]])
		mem_counts[max_pos[0]] = mem_counts[max_pos_temp]
		max_pos = max_pos + [max_pos_temp]
		print max_pos, mem_counts


	for i in range(len(mem_counts)):
		if max_pos.count(i) == 0:
			for j in range(mem_counts[i]//2):
				sol.append(lets[i]+lets[i])
			if mem_counts[i]%2 == 1:
				sol.append(lets[i])
	if len(max_pos) > 2:
		for k in range(len(max_pos) - 2):
			i = max_pos[k+2]
			for j in range(mem_counts[i]//2):
				sol.append(lets[i]+lets[i])
			if mem_counts[i]%2 == 1:
				sol.append(lets[i])

				
	for i in range(mem_counts[max_pos[0]]):
		
		sol.append(lets[max_pos[0]]+lets[max_pos[1]])
		
	
	print sol
	#for i in len(c):


	

	fout.write("Case #" + str(ii+1) + ": " + ' '.join(sol) + "\n")