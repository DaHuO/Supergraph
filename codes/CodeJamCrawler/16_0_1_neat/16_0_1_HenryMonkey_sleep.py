import sys
input = file(sys.argv[1]).readline


def solution(N):
	count = 0
	while N != 0 and N % 10 == 0:
		N /= 10
		count += 1
	if N == 0:
		return "INSOMNIA"
	ans = [0] * 10
	if count != 0:
		ans[0] = 1
	tmp = N
	while sum(ans) != 10:
		s = allDi(tmp)
		for i in range(10):
			ans[i] = ans[i] or s[i]
		tmp += N
	return str((tmp - N) * 10**count)
		

def allDi(N):
	ans = [0] * 10
	while N != 0:
		ans[N%10] = 1
		N /= 10
	return ans

for case in range(int(input())):
	N = int(input().strip())
	print "Case #%d: %s " % (case+1, solution(N)) 
