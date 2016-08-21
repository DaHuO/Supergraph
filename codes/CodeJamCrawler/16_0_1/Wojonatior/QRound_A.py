test_cases = []
test_num = 1
with open("A-large.in", "r") as f:
	num_cases = int(f.readline())
	for _ in range(num_cases):
		test_cases.append(int(f.readline()))
with open("QRound_A_large.txt", "w") as f:

	for test_case in test_cases:
		is_in_pattern = [False] * 10

		for i in range(1,100):
			NUT = str(test_case * i)

			for char in NUT:
				is_in_pattern[int(char)] = True

			if (is_in_pattern.count(True) == 10):
				f.write("Case #" + str(test_num) + ": " + NUT + "\n")
				print("Case #" + str(test_num) + ": " + NUT)
				break

		if is_in_pattern.count(True) < 10:
			f.write("Case #" + str(test_num) + ": INSOMNIA\n")
			print("Case #" + str(test_num) + ": INSOMNIA")
		test_num += 1

