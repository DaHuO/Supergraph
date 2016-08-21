T = int(input())
for t in range(T):
	print("Case #" + str(t+1) + ": ",end="")
	s = input()
	# print(s)
	somme = 0
	first = True
	prec = "+"
	for i in reversed(s):
		if (i!=prec):
			somme+=1
			prec = i
	print(str(somme))