import math

def gera_primos(N):
	primos = [ 2 ]

	for k in range(3, N + 1, 2):
		primo = True

		for p in primos:
			if k % p == 0:
				primo = False
				break
			if p > 1 + math.sqrt(k):
				break

		if primo:
			primos.append(k)

	return primos

def conv(S, b):
	acc = 0
	S = '1' + S + '1'

	for i in range(len(S)):
		if S[i] == '1':
			acc += b ** i

	return acc

def is_primo(primos, N):
	for p in primos:
		if N % p == 0:
			return p

		if p > 1 + math.sqrt(N):
			break

	return -1

# - - - - -

Q = gera_primos(2000000)

T = int(raw_input())
C = 1

while T > 0:
	T -= 1

	O = (raw_input()).split()

	N = int(O[0])
	J = int(O[1])

	X = [0 for i in range(N - 2)]

	print "Case #" + str(C) + ":"
	C += 1

	j = 1
	cont = 0
	while j < 2 ** (N - 2) and cont < J:
		j += 1

		L = [ ]
		yeah = True

		for b in range(2, 10 + 1):
			y = is_primo(Q, conv(''.join(str(k) for k in X), b))
			if y > 0:
				L.append(y)
			else:
				yeah = False
				break

		if yeah:
			cont += 1
			print ('1' + ''.join(str(k) for k in X) + '1')[::-1],
			
			for k in L:
				print k,
			print

		if len(X) > 0:
			X[0] += 1
			for i in range(len(X) - 1):
				if X[i] > 1:
					X[i + 1] += 1
					X[i] = 0