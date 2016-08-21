import sys

def run(num):
	current = num
	multiplier = 1
	counting_numbers = [0,1,2,3,4,5,6,7,8,9]
	seen = set(counting_numbers)

	def check(num, seen):
		for number in str(num):
			seen.discard(int(number))

	if current == 0:
		return "INSOMNIA"
	else:
		while seen:
			current = num*multiplier
			multiplier+=1
			check(current, seen)
		return str(current)

N = []
input_file = sys.argv[1]
with open(input_file) as f:
	f.next()
	for line in f:
		N.append(int(line))

print N
# main method handler
for i, num in enumerate(N):
	print "Case #" + str(i+1) + ": " + run(num)