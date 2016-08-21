import sys

if (len(sys.argv) < 2):
	print "Need inputfile as argument"
	exit(1)

#read file
input = list()
with open(sys.argv[1], 'r') as f:
	input = f.read().splitlines()
input.pop(0)

#convert to 0/1 list
d = dict({'+' : True, '-' : False})
input = map(lambda s: map(lambda c: d[c], s), input)

#compute
output = list()
for task in input:
	n = 0
	prev = task[-1]
	# if the first symbol is -, we need to flip it
	if (not prev):
		n = 1
	for position in reversed(task[:-1]):
		# consider flipping only if the pancake has 
		# another orientation than the previous one
		if position != prev:
			prev = position
			# flip if the current pancake is blank
			# or started out as chocolate, but was flipped
			if ((not position) or (n % 2 == 1)):
				n += 1
	output.append(n)



#write file
with open('output.txt', 'w') as f:
	for (line, index) in zip(output, range(1,len(output)+1)):
		f.write("Case #"+str(index)+": "+str(line)+"\n")
