f = open('large1.in')
T = int(f.readline().strip())
# print T

wins = {'R':'RS', 'S':'PS', 'P':'PR'}

for k in range(T):
	test = f.readline().split()
	N = int(test[0])
	R = int(test[1])
	P = int(test[2])
	S = int(test[3])

	total = 2**N
	each = total/3
	if R < each or R > each + 1:
		print "Case #%d: IMPOSSIBLE" %(k+1)
		continue
	if P < each or P > each + 1:
		print "Case #%d: IMPOSSIBLE" %(k+1)
		continue
	if S < each or S > each + 1:
		print "Case #%d: IMPOSSIBLE" %(k+1)
		continue
	Rwin = R
	Rwins = ['R'] * R
	Pwin = P
	Pwins = ['P'] * P
	Swin = S
	Swins = ['S'] * S
	while (total > 1):
		if (Rwin%2==0):
			even = 'R'
			Rwin = Rwin/2
			Swin = Swin - Rwin
			Pwin = Pwin - Swin
		elif (Swin%2==0):
			even = 'S'
			Swin = Swin/2
			Pwin = Pwin - Swin
			Rwin = Rwin - Pwin
		elif (Pwin%2==0):
			even = 'P'
			Pwin = Pwin/2
			Rwin = Rwin - Pwin
			Swin = Swin - Rwin
		Pwintemp = []
		Rwintemp = []
		Swintemp = []
		for i in range(Pwin):
			if Pwins[0] < Rwins[0]:
				Pwintemp.append(Pwins[0] + Rwins[0])
			else:
				Pwintemp.append(Rwins[0] + Pwins[0])
		for i in range(Rwin):
			if Rwins[0] < Swins[0]:
				Rwintemp.append(Rwins[0] + Swins[0])
			else:
				Rwintemp.append(Swins[0] + Rwins[0])
		for i in range(Swin):
			if Pwins[0] < Swins[0]:
				Swintemp.append(Pwins[0] + Swins[0])
			else:
				Swintemp.append(Swins[0] + Pwins[0])
		Pwins = Pwintemp
		Rwins = Rwintemp
		Swins = Swintemp
		total = total/2
	if Swin == 1:
		winner = Swins[0]
	elif Rwin == 1:
		winner = Rwins[0]
	elif Pwin == 1:
		winner = Pwins[0]
	# while total < 2**N:
	# 	new = ''
	# 	for i in winner:
	# 		new += wins[i] 
	# 	winner = new
	# 	total = total*2
	print "Case #%d: %s" %(k+1, winner)



