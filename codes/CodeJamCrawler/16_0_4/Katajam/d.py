

def solution(k, c, s):
	if c*s < k: return 'IMPOSSIBLE'
	else: return ' '.join(list(map(str, range(1, s+1))))

n = int(input())
for i in range(n):
	data = list(map(int, input().split()))
	K, C, S = data[0], data[1], data[2]

	print('Case #{}: {}'.format(i+1, solution(K, C, S)))



