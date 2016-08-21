import math
t = input()
high = int(math.pow(10, 7))
for i in range(t):

	n = input()
	ans = []
	if n == 0:

		print "Case #" + str(i + 1) + ": " + "INSOMNIA"
		continue

	ml = 1
	count = 0

	while True:

		num = n * ml
		if num > high:
			print "Case #" + str(i + 1) + ": " + "INSOMNIA"
			break
		temp = list(str(num))

		for j in temp:

			if j not in ans:
				ans.append(j)
		
		count += 1

		if len(ans) == 10:
			print "Case #" + str(i + 1) + ": " + str(num)
			break

		ml += 1
