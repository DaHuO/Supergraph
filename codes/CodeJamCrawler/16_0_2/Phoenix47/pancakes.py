from collections import deque
import copy

def flip(p, index):
	flip = [[c[0] ^ 1, c[1]] for c in reversed(p[:index])]
	stay = copy.deepcopy(p[index:])
	if (flip and stay and flip[-1][0] == stay[0][0]):
		stay[0][1] += flip.pop()[1]
	return flip + stay


def check_happy(p):
	return len(p) == 1 and p[0][0] == 1

def make_mutable(s):
	arr = []
	last = None
	value = None
	for c in s:
		if (c == '+'):
			value = 1
		else:
			value = 0
		if (value == last):
			arr[-1][1] += 1
		else:
			arr.append([value, 1])
			last = value
	return arr

def rindex(p, value):
	i = len(p)
	for c in reversed(p):
		if (c[0] == value): return i
		i -= 1

def flip_pancakes(s):
	p = make_mutable(s)
	i = 0
	queue = deque()
	queue.append((i,p))
	max_tail = 0
	while (queue):
		i,p = queue.popleft()
		if (max_tail > 0 and p[-1][1] < max_tail):
			continue
		# print(i, p)
		if (check_happy(p)):
			return i
		for index in range(1, rindex(p,0) + 1):
			new_p = flip(p, index)
			tail_node = new_p[-1]
			if (tail_node[0] == 1):
				if (tail_node[1] < max_tail):
					continue
				else:
					max_tail = tail_node[1]
			queue.append((i+1, new_p))
	return False

if __name__ == "__main__":
	t = int(input())
	for i in range(1, t + 1):
		s = input()
		print("Case #{}: {}".format(i, flip_pancakes(s)))
