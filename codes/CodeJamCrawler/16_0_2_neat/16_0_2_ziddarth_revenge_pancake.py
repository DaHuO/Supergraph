
def main():
	t = int(input())
	case = 1
	while case <= t:
		pancakes = raw_input().strip()
		n = len(pancakes)
		count = sum([1 for i in range(1, n) if pancakes[i] != pancakes[i-1]])
		if pancakes[-1] == '-':
			count += 1
		print 'Case #{}: {}'.format(case, count)
		case += 1


if __name__ == '__main__':
	main()