def pancake(order):
	#start from the back, and every time a  - appears, flip everything from that to the top, 
	#continue this until everything is +
	flip = 0
	good, bad = '+', '-'
	index = len(order)
	for i in range(len(order)-1, -1, -1):
		if order[i] == bad:
			flip += 1
			good, bad = bad, good
	return flip		



file = open("B-large.in")
data = file.readlines()
trials = int(data[0].strip('\n'))

for i in range(1, trials+1):
	order = data[i].strip('\n')
	print "CASE #"+str(i)+": "+str(pancake(order))	