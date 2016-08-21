import sys

fileout = sys.stdout
cases = int(raw_input())

for case in range (0, cases):
	n = raw_input()
	i = 1
	check = []
	check.append(int(n[0]))
	
	if int(n) == 0:
		print ("Case #{}: INSOMNIA".format(case + 1))
	else:
		while len(check) < 10:
			next = str(int(n) * (i))
			for y in range (0, len(next)):
				number = next[y]
				same = 0
				# iterate number in input
				for z in range (0, len(check)):
					if int(number) == int(check[z]):
						same += 1
				if same == 0:
					check.append(int(number))
			i += 1
		print ("Case #{}: {}".format(case + 1, next))