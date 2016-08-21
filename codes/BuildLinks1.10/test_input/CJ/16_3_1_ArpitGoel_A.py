ALPHA = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
f = open('input', 'r')
g = open('output', 'a')
T = int(f.readline())
for i in range(T):
	N = int(f.readline())
	Senates = []
	temp = [int(t) for t in f.readline().strip("\n").split(" ")]
	for j in range(0, len(temp), 1):
		Senates.append([ALPHA[j], temp[j]])
	plan = []
	while max(Senates, key = lambda x: x[1])[1] > 0:
		Senates.sort(key = lambda x: x[1])
		if Senates[len(Senates) - 1][1] == Senates[len(Senates) - 2][1]:
			if Senates[len(Senates) - 1][1] > 1 :
				Senates[len(Senates) - 1][1] -= 1
				Senates[len(Senates) - 2][1] -= 1
				plan.append(str(Senates[len(Senates) - 1][0]) + str(Senates[len(Senates) - 2][0]))
			else:
				if len(Senates) > 2 and Senates[len(Senates) - 3][1] > 0:
					Senates[len(Senates) - 1][1] -= 1
					plan.append(str(Senates[len(Senates) - 1][0]))
				else:
					Senates[len(Senates) - 1][1] -= 1
					Senates[len(Senates) - 2][1] -= 1
					plan.append(str(Senates[len(Senates) - 1][0]) + str(Senates[len(Senates) - 2][0]))
		else:
			if Senates[len(Senates) - 1][1] > 1:
				Senates[len(Senates) - 1][1] -= 2
				plan.append(str(Senates[len(Senates) - 1][0]) + str(Senates[len(Senates) - 1][0]))
			else:
				Senates[len(Senates) - 1][1] -= 1
				plan.append(str(Senates[len(Senates) - 1][0]))
	
	g.write("Case #{0}: {1}\n".format(i+1, " ".join([str(x) for x in plan])))