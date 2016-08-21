import os

tour = int(input())

for case in range(1, tour+1):
	i = 1
	listall = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	listdigit = [-1] * 10
	n = int(input())
	if n == 0:
		last = "INSOMNIA"
		listdigit = listall
	while listdigit != listall:
		last = n*i
		x = n*i
		while x > 0:
			digit = x % 10
			if digit not in listdigit:
				listdigit[digit] = digit
			x = int(x/10)

		i += 1

	print("Case #" + str(case) + ": " + str(last))

os.system("pause")