input = []

f = open('A-large.in', 'r')
T = int(f.readline()) # T = num test cases.
for i in range(T):
	input.append(int(f.readline()))
f.close()

for x in range(len(input)):
	N = input[x]
	if N == 0:
		print "Case #%s: INSOMNIA" % (x+1)
		continue
	digits = "0123456789"
	iter = 1
	while digits:
		y = str(N*iter) # Number being viewed.
		for d in y:
			digits = digits.replace(d, "")
		iter += 1

	print "Case #%s: %s" % (x+1, y)
