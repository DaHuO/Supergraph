tests = int(input())
for _ in range(tests):
	s = input().split(" ")
	k = int(s[0])
	c = int(s[1])
	s = int(s[2])
	checks = []
	for i in range(0, k ):
		checks.append(i * (k**(c-1)) + 1)
	print("Case #" + str( _ + 1) + ":", end=" ")
	for c in checks:
		print(c, end=" ")
	print()