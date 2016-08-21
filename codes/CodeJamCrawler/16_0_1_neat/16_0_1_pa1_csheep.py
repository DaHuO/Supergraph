def f(n):
	dc = 0
	i = 1
	dm = {}
	cn = n
	while not len(dm) == 10:
		mn = n * i
		rmn = str(mn)
		for d in rmn:
			dm[int(d)] = True
			dm[int(d)] = True
		i = i + 1
	i = i - 1
	return n * i

def main():
	T = raw_input()
	T = int(T)
	t = 1
	while t <= T:
		x = int(raw_input())
		if x == 0:
			print "Case #{0}: INSOMNIA".format(t)
			t = t + 1
			continue

		ans = f(x)
		print "Case #{0}: {1}".format(t, ans)
		t = t + 1

if __name__ == "__main__":
	main()