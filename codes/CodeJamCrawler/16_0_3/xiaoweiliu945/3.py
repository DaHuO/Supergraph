def genetate_Init(n):
    if n == 2:
        return ['11']

    res = []
    tmp = [1 for i in range(n-2)]
    upper_bound = ''.join(str(x) for x in tmp)
    count = int(upper_bound, 2) + 1
    for i in range(0, count):
        tmp = str(bin(i))[2:]
        if len(tmp) < n-2:
            for j in range(n-2-len(tmp)):
                tmp = '0' + tmp
        tmp = '1' + tmp + '1'
        res.append(tmp)

    return res
    
def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return i
    return 0

def jamcode(n):
	for num in genetate_Init(n):
		jamcoins = []
		for i in range(2, 11):
			tmp = isPrime(int(num, i))
			if tmp == 0:
				break
			else:
				jamcoins.append(tmp)
		if len(jamcoins) < 9:
			continue
		else:
			yield num + ' ' + ' '.join(str(x) for x in jamcoins)



t = int(raw_input())
for i in range(t):
	n, j = [int(x) for x in raw_input().split(' ')]
	print 'Case #%d:'%(i+1)
	ob = jamcode(n)
	for x in range(j):
		print next(ob)