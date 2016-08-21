T = int(raw_input())
C = 1

while T > 0:
	T -= 1
	S = raw_input()

	print "Case #" + str(C) + ":",
	C += 1
	
	cont = 0
	if len(S) > 1:
		for k in range(len(S) - 1):
			if S[k + 1] != S[k]:
				cont += 1
	if S[-1] == '-':
			cont += 1

	print cont