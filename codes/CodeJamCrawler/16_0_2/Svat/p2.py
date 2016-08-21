import sys

def solve(s):
	check = '-'
	arr = [0 for c in s]
	l = len(arr)
	if s[-1] == '-':
		arr[-1] = 1
		check = '+'
	for i in range(1,len(arr)):
		if s[l-i-1]==check:
			arr[l-i-1] = arr[l-i] + 1
			check = '+' if check == '-' else '-'
		else:
			arr[l-i-1] = arr[l-i]
	return arr[0]

if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)

    N = int(f.readline().strip())
    for i in xrange(N):
        x = solve(f.readline().strip())
        print("Case #%d: %d" % (i+1, x))