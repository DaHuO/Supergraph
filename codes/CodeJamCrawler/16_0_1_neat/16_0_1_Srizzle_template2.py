import sys
# dic = {}

# for i in range(1, 100):
# 	count = 0
# 	currnumber = 0 
# 	notseen = list(hit)
# 	while( notseen != []):
# 		count+=1 
# 		currnumber+= i
# 		compare = [int(j) for j in str(currnumber)]
# 		for k in compare:
# 			if k in notseen:
# 				notseen.remove(k)

# 	dic[i] = count



# def sleep(n): 
# 	maxnumber = dic[n % 100]
hit = [0,1,2,3,4,5,6,7,8,9]

f = open('A-large.in', 'r')
w = open('outputfile', 'w')

T = int(f.readline())
for i in range(0,T):
	temp = f.readline()
	N = int(temp)
	if N ==0: 
		w.write("Case #" + str(i+1) + ": " + "INSOMNIA" + "\n")
	else: 
		count = 0
		currnumber = 0 
		notseen = list(hit)
		while( notseen != []):
			count+=1 
			currnumber+= N
			compare = [int(j) for j in str(currnumber)]
			for k in compare:
				if k in notseen:
					notseen.remove(k)
		w.write("Case #" + str(i+1) + ": " + str(N*count)+"\n")
w.close()	
	
	









