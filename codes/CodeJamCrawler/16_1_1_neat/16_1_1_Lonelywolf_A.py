def print_ans(case_num, ans):
	print('Case #%d: %s' % (case_num, ans))


	
cache = {}
T = int(input())
for t in range(T):
	S = input()
	ans = ''
	for s in S:
		if len(ans) == 0:
			ans = s
		else:
			if ans[0] > s:
				ans = ans + s
			else:
				ans = s + ans

	print_ans(t+1, ans)