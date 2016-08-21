# -*- coding:utf-8 -*-
import sys
import random
sys.setrecursionlimit(10000)

def flip(stack):
	
	res = ''
	for e in stack:
		if e == '+':
			res += '-'
		else:
			res += '+'
	return res[::-1]

def non_alternate(stack):
	if len(stack) == 0:
		return True

	seen = stack[0]
	non_alternate = True
	sign_changed = False
	for e in stack[1:]:
		if e != seen and sign_changed == False:
			sign_changed = True
			seen = e
		elif e != seen and sign_changed == True:
			non_alternate = False
			break

	return non_alternate

def generate_random_input(n):
	res = ''
	for _ in range(n):
		x = random.random()
		if x > 0.5:
			res += '-'
		else:
			res += '+'
	return res

def solve_greedy(stack):

	ans = 0
	cur = stack[0]
	for e in stack[1:]:
		if e != cur:
			ans += 1
			cur = e
	if cur == '-':
		ans += 1

	return ans

def solve_exaustive(stack, cur_flip, dp, ans_dp):
	# 팬케익을 뒤집다가 이미 만나본걸 또 만났는데 아직 답은 못구한 케이스.
	# print 'am considering stack {0}, at depth {1}'.format(stack, cur_flip)
	if stack in dp and dp[stack] < cur_flip:
		# print 'has already seen this case but not done {0}'.format(stack)
		return 987654321
	
	# 이미 답을 구한 케이스.
	if stack in ans_dp:
		# print 'already solved this subproblem {0}'.format(stack)
		return ans_dp[stack]
	
	# 모두 +이므로 더이상 뒤집을 필요가 없는 케이스.
	if stack == '+'*len(stack):
		ans_dp[stack] = 0
		return 0

	# ------++++++ 이거나 +++++----------인 형태이면 바로 1번, 2번안에 끝낼 수 있다.
	if non_alternate(stack):
		# print 'non alternate found. {0}'.format(stack)
		if stack[0] == '-':
			ans_dp[stack] = 1
			return 1
		else:
			ans_dp[stack] = 2
			return 2

	dp[stack] = cur_flip
	
	ans = 987654321
	for idx in range(len(stack)):
		# 앞에서부터 뒤집어본다.
		prefix_flipped = flip(stack[:idx+1])
		new_stack = prefix_flipped + stack[idx+1:]

		# 뒤집었는데 같으면 무시한다.
		if new_stack == stack:
			continue
		ans = min(ans, solve_exaustive(new_stack, cur_flip+1, dp, ans_dp))

	ans_dp[stack] = 1 + ans
	return ans + 1

f_out = open('B_output.txt', 'w')
f_in = open('B-large.in', 'r')

lines = [line.strip() for line in f_in.readlines()][1:]
for idx in range(len(lines)):
	f_out.write("Case #{0}: {1}\n".format(idx+1, solve_greedy(lines[idx])))

f_out.close()
