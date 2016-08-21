import string
import operator

def preveri(raz, c):
	if(c == 0): return True
	for k,v in dis:
		if(float(v)/float(c) > 0.5000000000):
			#print "#########################"
			#print dis, float(v)/float(c)
			#print "#########################"
			return False
	return True

def prazno(raz):
	for k,v in raz:
		if(v > 0):
			return False
	return True

t = int(raw_input())

crke = string.ascii_uppercase
for test in range(t):
	n = int(raw_input())
	senate = map(int, raw_input().split())
	c = 0
	di = {}
	rez = ""
	for i in range(len(senate)):
		di[crke[i]] = senate[i]
		c += senate[i]
	
	#dis = sorted(di.items(), key=operator.itemgetter(1), reverse = True)
	#print dis
	#print c

	while True:
		
		dis = sorted(di.items(), key=operator.itemgetter(1), reverse = True)
		#print c, dis, di
		if(prazno(dis)):
			print "Case #{0}: {1}".format(test + 1, rez[:-1])
			break
		if(dis[0][1] - 2 >= dis[0][1]):
			dis[0] = (dis[0][0], dis[0][1] - 2)
			c-=2
			if(preveri(dis,c)):
				rez += 2*dis[0][0] + " "
				di[dis[0][0]] -= 2
				continue
			else:
				dis[0] = (dis[0][0], dis[0][1] + 2)
				c+=2
		if(dis[0][1] >= 1 and dis[1][1] >= 1):	
			dis[0] = (dis[0][0], dis[0][1] - 1)
			dis[1] = (dis[1][0], dis[1][1] - 1)
			c-=2

			if(preveri(dis,c)):
				rez += dis[0][0] + dis[1][0]  + " "
				di[dis[0][0]] -= 1
				di[dis[1][0]] -= 1
				continue
			else:
				dis[0] = (dis[0][0], dis[0][1] - 1)
				dis[1] = (dis[1][0], dis[1][1] - 1)
				c+=2


		dis[0] = (dis[0][0], dis[0][1] - 1)
		c-=1
		rez += dis[0][0]  + " "
		di[dis[0][0]] -= 1


		