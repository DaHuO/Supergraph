import sys
	
if __name__ == "__main__":

	tests = int(sys.stdin.readline())
	
	for test in range(1, tests + 1):
		n = int(sys.stdin.readline().replace("\n", ""))
		d = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
		ans = "INSOMNIA"
		if n != 0:
			for i in range(1, 1000000):
				count = n * i
				for c in str(count):
					if c in d:
						d.remove(c)
				if len(d) == 0:
					ans = count
					break

		print ("Case #" + str(test) + ": " + str(ans))
