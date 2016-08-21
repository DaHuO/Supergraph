def get_i(N):
	a = set()
	i = 1
	if N == 0:
		return "INSOMNIA"
	odd = N % 2
	while i < 5000000:
		a.update(str(N*i))
		if len(a) == 10:
			return i*N
		i += 1
	return -1

T = int(input())
for i in range(1,T+1):
	N = int(input())
	print("Case #{}: {}".format(i, get_i(N)))
	
