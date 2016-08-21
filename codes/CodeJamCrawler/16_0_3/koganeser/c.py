def is_prime(n):
	i = 2;
	while i * i <= n:
		if n % i == 0:
			return [False, i]
		i += 1
	return [True, -1]

def to_p(n, p):
	res = 0
	for cd in range(20):
		if (n >> cd) & 1:
			res += p ** cd
	# print(n, p, res)
	return res

res = 0
out = open("out", "w")
print("Case #1:", file=out)
for i in range(2 ** 15 + 1, 2 ** 100, 2):
	if res == 50:
		break
	good = True
	ans = []
	for p in range(2, 11):
		cres = is_prime(to_p(i, p))
		if cres[0]:
			good = False
			break
		else:
			ans.append(cres[1])
	if good:
		res += 1
		print("{0:b} ".format(i), sep="", end='', file=out)
		print(*ans, file=out)