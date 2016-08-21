from itertools import product
def factor(n):
    if n == 2:
        return None
    if n == 3:
        return None
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return i
        i += w
        w = 6 - w

    return None


nans = 0
input()
n, j = map(int, input().split())
print('Case #1')
for i in product('01', repeat=n-2):
	s = '1' + ''.join(i) + '1'
	div = []
	for base in range(2, 11):
		a = int(s, base)
		#print(a)
		fact = factor(a)
		if fact is None:
			break
		div.append(fact)
	else:
		print(s, ' '.join(map(str, div)))
		nans += 1
		if nans == j:
			break
