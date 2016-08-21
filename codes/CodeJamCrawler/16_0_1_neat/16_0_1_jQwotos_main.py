class Fuller:
	def __init__(self):
		self.set = dict()
		for i in range(10):
			self.set[i] = False

	def reset(self):
		for i in range(10):
			self.set[i] = False

full_set = Fuller()

with open("input.txt") as f:
	with open("output.txt", "w+") as out:
		next(f)
		currentTest = 1
		for line in f:
			t = 1
			n = int(line)
			while True:
				num = t * n
				if num > 0:
					for singleNum in str(num):
						full_set.set[int(singleNum)] = True
				else:
					out.write("Case #" + str(currentTest) + ": INSOMNIA\n")
					#print("Case #", str(currentTest), ": INSOMNIA")
					break
				if all(x==True for x in full_set.set.values()):
					out.write("Case #" + str(currentTest) + ": " + str(num) + "\n")
					#print("Case #" + str(currentTest) + ":" + str(num))
					break
				t += 1
			full_set.reset()
			currentTest += 1

		f.close()