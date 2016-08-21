t = int(input())

for test in range(t):
	print('Case #' + str(test + 1)  + ': ', end='')
	K, C, S = map(int, input().split())
	print(*[i for i in range(1, S+1)])