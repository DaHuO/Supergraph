
# returns list of tuples
def findseeds(bff):  # at least 3 items. bff[0] is dummy

	seedlines = {}
	n = len(bff)
	result = {}
	for i in xrange(1,n-1):
		for j in xrange(i+1, n):
			if bff[i] == j and bff[j] == i:
				seedlines[(i,j)]= [i,j]
				seedlines[(j,i)]= [j,i]
	return seedlines

def calc(bff):
	maxcircle = []
	n = len(bff)
	seedlines = findseeds(bff)  # seed(tuple) to sequence. last two shoud be seed
	for i in xrange(1,n):  # explore starting from i
		seq = [i,bff[i]]  #seq is always added ones. so no repitition
		i = bff[i]
		while True:  #we already added item i. we are checking.
			last2 = tuple(seq[-2:])
			if last2 in seedlines: # we found a seed
				if len(seedlines[last2]) < len(seq):
					seedlines[last2] = seq
				break
			#print bff,i,seq
			if bff[i] == seq[0]: # we found a circle
				if len(seq) > len(maxcircle):
					maxcircle = seq
				break
			if bff[i] in seq: #no circle. break
				break

			# we are moving forward
			i = bff[i]
			seq += [i]
		

	seedmax = 0
	for i in xrange(1,n-1):
		for j in xrange(i+1, n):
			if (i,j) in seedlines:
				seedmax += (len(seedlines[(i,j)]) + len(seedlines[(j,i)]) -2)


	return max(seedmax,len(maxcircle))
	#return maxcircle, seedlines, seedmax, max(seedmax,len(maxcircle))

t = int(raw_input())  
for i in xrange(1,t+1):
  raw_input()
  bff = map(int,raw_input().split(" "))
  print "Case #{}: {}".format(i, calc( [0] + bff))
  