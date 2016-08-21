from collections import deque, Counter


def main():
	T = int(raw_input())
	case = 1
	numbers = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
	while case <= T:
		s = raw_input()
		chars = Counter(s)
		q = deque()
		q.append((chars, 0, []))
		answer = None
		while q:
			current, i, l = q.popleft()
			if not current:
				answer = l
				break
			for j, number in enumerate(numbers[i:], i):
				new_current = Counter(current)
				for c in number:
					if c not in new_current:
						break
					new_current[c] -= 1
					if new_current[c] == 0:
						new_current.pop(c)
				else:
					new_l = l[:]
					new_l.append(str(j))
					q.append((new_current, j, new_l))

		print 'Case #{}: {}'.format(case, ''.join(answer))

		case += 1

if __name__ == '__main__':
	main()

