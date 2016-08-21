import itertools

N = 32 
J = 500

i = 0

ans = []

for var in (itertools.product([0, 1], repeat = N - 2)):
	number = int("".join([str(x) for x in var]))
	if number % 11 == 0:
		ans += [number] 
		i += 1  
	if i >= J:
		break

print "Case #1:"

x = pow(10, N - 1) + 1

for a in ans:
	cur_ans = [x + 10 * a] + range(3, 12)
	print " ".join("{0}".format(n) for n in cur_ans)

