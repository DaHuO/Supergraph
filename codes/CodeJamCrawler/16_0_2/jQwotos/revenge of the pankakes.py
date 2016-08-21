with open("input.txt") as f:
	with open("output.txt", "w+") as out:
		next(f)
		case = 1
		for line in f:
			storage = []
			trials = 0
			for character in line:
				if character == "-":
					storage.append(-1)
				elif character == "+":
					storage.append(1)
			while True:
				#print(storage)
				for cha in range(len(storage) -1 , -1, -1):
					if storage[cha] < 0:
						trials += 1
						for x in range(cha, -1, -1):
							storage[x] *= -1
				if all(x>0 for x in storage):
					out.write("Case #" + str(case) + ": " + str(trials) + "\n")
					#print("Case #" + str(case) + ": " + str(trials) + "\n")
					break
			case += 1
		f.close()