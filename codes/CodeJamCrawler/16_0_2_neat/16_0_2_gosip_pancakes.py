def main():
	f = open("B-large.in", "r")
	t = int(f.readline())
	for i in range(t):
		r = count(f.readline().strip())
		print("Case #" + str(i+1) + ": " + str(r))

def count(arg):
	cnt = 0
	last = arg[0]
	for c in arg:
		if last == '-' and c == '+':
			last = '+'
			cnt += 1
		elif last == '+' and c == '-':
			last = '-'
			cnt += 1
	if arg[len(arg) - 1] == '-':
		cnt += 1
	return cnt

if __name__ == '__main__':
	main()