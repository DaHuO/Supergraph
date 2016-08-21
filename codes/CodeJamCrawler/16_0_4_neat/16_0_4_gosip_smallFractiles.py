def main():
	f = open('D-small-attempt0.in', 'r')
	t = int(f.readline())
	for i in range(t):
		k,c,s = [int(x) for x in f.readline().strip().split(' ')]
		step = k ** (c-1)
		ans = [1]
		for j in range(s-1):
			ans.append(ans[-1] + step)
		asString = ' '.join([str(x) for x in ans])
		print("Case #" + str(i+1) + ": " + asString)

if __name__ == '__main__':
	main()