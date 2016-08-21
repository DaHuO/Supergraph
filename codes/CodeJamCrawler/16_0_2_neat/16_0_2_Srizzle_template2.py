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


f = open('B-large.in', 'r')
w = open('outputfile', 'w')

T = int(f.readline())
for i in range(1,T+1):
	temp = f.readline()
	
	if temp[0] == '-':
		pos = [1]
		neg = [0] 
	if temp[0] == '+':
		pos = [0]
		neg = [1]
	for j in range(1, len(temp)):
		if temp[j] == '-':
			posvalue = min( pos[j-1] +2, neg[j-1] + 1)
			negvalue = min(neg[j-1], pos[j-1] + 1)
			pos.append(posvalue)
			neg.append(negvalue)
		if temp[j] == '+':
			posvalue = min( pos[j-1], neg[j-1] + 1 )
			negvalue = min( pos[j-1] +1, neg[j-1] + 2)
			pos.append(posvalue)
			neg.append(negvalue)
	w.write("Case #" + str(i) + ": " + str(pos[-1])+"\n")
w.close()	
	
	









