#input_file = "input_test.in"
#input_file = "B-small-attempt0.in"
input_file = "B-large.in"
#output_file = "output_test.out"
#output_file = "output_small.out"
output_file = "output_large.out"



with open (input_file,'r') as input, open(output_file,'w') as output:
	num_cases = int(input.readline().strip())
	for i in range(num_cases):
		count = 0
		pancakes = list(input.readline())
		if "\n" in pancakes:
			pancakes.remove("\n")
		for j in range (len(pancakes)-1):
			if pancakes[j] != pancakes[j+1]:
				count += 1
				for k in range(j+1):
					if pancakes[k] == "-":
						pancakes[k] = "+"
					elif pancakes [k] == "+":
						pancakes[k] = "-"
		if pancakes[0] == "-":
			count += 1
			for l in range(len(pancakes)):
				if pancakes[l] == "-":
					pancakes[l] = "+"
		output.write("Case #{0}: {1}\n".format(i+1,count))