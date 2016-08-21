def pancakes():
	input = open('B-large.in')
	test_cases = int(input.readline()) + 1
	result_file = open('resultsB.txt', 'w')

	print test_cases

	for iterator in range(1,test_cases):
			x = 0
			N = input.readline().rstrip()
			no_of_pancakes = int(len(list(N)))
			if no_of_pancakes == 1:
				if N[0] == '-':
					N = list(N)
					N[0] = "+"
					print >> result_file, "Case #%d: %s" % (iterator, 1)
				elif N[0] == '+':
					print >> result_file, "Case #%d: %s" % (iterator, 0)
		

					
			else:
				x = 1
				flips = 0
				result = N

				while x:
					count = 0
					for m in range(0,len(result)):
						if result[m] == '+':
							count = count + 1
					
					if count == no_of_pancakes:
						break
					for i in range(no_of_pancakes-1,-1,-1):
						if result[i] == '-':
							index = i
							rev_part1 = result[0: i + 1]
							if rev_part1[0] == '-' and rev_part1[1:len(rev_part1)] == (['+'] * (len(rev_part1) - 1)) and len(rev_part1) != 2:
								rev_part1 = ['-'] * len(rev_part1)
							else:
								rev_part1 = list(rev_part1)
								for g in range(0,len(rev_part1)):
									if rev_part1[g] == '+':
										rev_part1[g] = "-"
									elif rev_part1[g] == '-':
										rev_part1[g] = "+"
							part1 = ''.join(rev_part1)
							part2 = result[i + 1::]
						 	result = part1 + part2
							flips += 1
							break
				print >> result_file, "Case #%d: %s" % (iterator, flips)
	
if __name__ == "__main__":
	pancakes()












	
