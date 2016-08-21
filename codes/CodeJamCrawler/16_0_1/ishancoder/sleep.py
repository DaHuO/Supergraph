def check_all_numbers(number, l):
	while number > 0:
		x = number % 10
		try:
			pos = l.index(x)
			if pos >= 0:
				l.pop(pos)
		except ValueError as e:
			pass
		number = number // 10


test_case = int(input())

for _ in range(test_case):
	numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	i = 1
	N = int(input())
	print("Case #"+str(_+1)+":" , end=" ")
	if N == 0:
		print("INSOMNIA")
	else:
		while numbers != []:
			check_all_numbers(i*N, numbers)
			i=i+1
		print((i-1)*N)

