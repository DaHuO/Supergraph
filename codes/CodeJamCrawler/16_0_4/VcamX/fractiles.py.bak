from itertools import combinations

def tile_at(original, k, c, p):
	relative_pos = []
	count = c
	for i in range(c):
		relative_pos.append(p % k)
		p //= k
	for i in reversed(relative_pos):
		if (original & (1 << i)) == 0:
			return 0
	return 1

def solve(k, c, s):
	if k == s:
		return ' '.join(list(map(lambda x: str(x), range(1, s+1))))
	for chosen in combinations(range(k ** c), s):
		count = 0
		for i in range(1, (2 ** k) - 1):
			for j in range(s):
				if tile_at(i, k, c, chosen[j]) == 0:
					count += 1
					break
		if count == 2 ** k - 2:
			return ' '.join(list(map(lambda x: str(x+1), chosen)))
	return 'IMPOSSIBLE'


t = int(input())
for i in range(1, t+1):
	k, c, s = [int(s) for s in input().split(' ')]
	print('Case #{}: {}'.format(i, solve(k, c, s)))
