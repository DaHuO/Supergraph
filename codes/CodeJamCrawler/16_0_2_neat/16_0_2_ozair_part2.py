def part2():
	file = open('B-large.in')
	num_of_cases = file.readline()
	output_file = open('output.txt', 'w')
	i = 1
	print num_of_cases
	while i < int(num_of_cases) + 1:
		string = file.readline()
		check = False
		j = 0
		k = 1
		while not check:
			k += 1
			#print string
			for x in range(len(string)-1, -1, -1):
				if string[x] == '-':
					j = j + 1
					string = reverse(string[0:x + 1]) + string[x + 1::]
					break
			check = True
			for y in range(0,len(string)):
				if string[y] == '-':
					check = False 
		print >> output_file, "Case #%d: %s" % (i, j) 
		i = i + 1

def reverse(string):
	string = list(string[::-1])
	if string[len(string) - 1] == '-' and string[0:len(string) - 2] == (['+'] * (len(string) - 1)) and len(string) != 1:
		string = ['-'] * len(string)
	else:
		string = list(string[::-1])
		for x in range(0,len(string)):
			if string[x] == '-':
				string[x] = "+"
			else:
				string[x] = '-'
	return ''.join(string)

if __name__ == "__main__":
	part2()