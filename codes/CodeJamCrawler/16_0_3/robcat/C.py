import sys
import sympy

next(sys.stdin)
N, J = map(int, next(sys.stdin).split())
print("Case #1:")
jamcoins = 0
c = (1<<N-1)-1
while jamcoins<J:
	c += 2
	str_c = format(c, 'b')
	#print()
	#print(c, str_c)
	if len(str_c)>N:
		break
	divisors = []
	for base in range(2, 11):
		based = int(str_c, base)
		ds = sympy.ntheory.factor_.primefactors(based)[:-1]
		if ds:
			divisors.append(ds[0])
		else:
			break
	if len(divisors)==9:
		print(str_c, *divisors)
		jamcoins += 1



