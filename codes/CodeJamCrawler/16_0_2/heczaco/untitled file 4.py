import math
f = open('1.in', 'r')
o = open('1.out', 'w')

T = int(f.readline().strip())

	
for t in xrange(T):
	pancakes = f.readline()[::-1]
	numbers = 0
	for i in range(0, len(pancakes)):
		if ((pancakes[i]=='-' and numbers%2==0) or (pancakes[i]=='+' and numbers%2==1)):
			numbers = numbers+1

	out = "Case #" + str(t+1) + ": " + str(numbers) + "\n"
	o.write(out)
	