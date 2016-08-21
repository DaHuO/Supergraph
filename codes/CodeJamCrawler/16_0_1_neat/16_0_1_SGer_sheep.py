import sys

if (len(sys.argv) < 2):
	print "Need inputfile as argument"
	exit(1)

#read file
input = list()
with open(sys.argv[1], 'r') as f:
	input = f.read().splitlines()
input.pop(0)

#convert to int list
input = map(int, input)

#compute
output = list()
for task in input:
	# zero is the only number that when adding up never gets through all digits
	if task == 0:
		output.append("INSOMNIA")
	else:
		seen = [False]*10
		number = 0
		while(not all(seen)):
			number += task
			for digit in str(number):
				seen[int(digit)] = True
		output.append(number)
#write file
with open('output_sheep.txt', 'w') as f:
	for (line, index) in zip(output, range(1,len(output)+1)):
		f.write("Case #"+str(index)+": "+str(line)+"\n")
