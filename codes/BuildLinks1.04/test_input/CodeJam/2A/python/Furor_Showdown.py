
def gen(n, C, r):
	if n == 0:
		return [ 1 if i == r else 0 for i in range(3) ], C[r]
	A1, s1 = gen(n - 1, C, r)
	A2, s2 = gen(n - 1, C, (r + 1) % 3)
	return [ A1[i] + A2[i] for i in range(3) ], min(s1, s2) + max(s1, s2)

def check(n, N, C, r):
	A, s = gen(n, C, r)
	if A[0] == N[0] and A[1] == N[1] and A[2] == N[2]:
		return s
	return None

def solve(n, N, C):
	ans = None
	for i in range(3):
		here = check(n, N, C, i)
		if ans is None or (here and here < ans):
			ans = here
	if ans:
		return ans
	return 'IMPOSSIBLE'

t = int(input().strip())
for i in range(t):
	C = input().strip().split()
	print('Case #{}: {}'.format(i + 1, solve(int(C[0]), [int(C[3]), int(C[2]), int(C[1])], ['S', 'P', 'R'])))
