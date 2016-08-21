


def flip(x):
	return ['+' if xe == '-' else '-' for xe in x]

def goodPancake(x):
	for i in x:
		if i == '-': return False
	return True

def solution(x, num, last):
	# print(x, num, last)
	if goodPancake(x): return num
	if x[last] != '+': return solution(flip(x), num+1, last)
	else: return solution(x[:-1], num, last-1)


n = int(input())
for i in range(n):
	pancakes = list(input())
	print('Case #{}: {}'.format(i+1, solution(pancakes, 0, len(pancakes)-1)))

