file = open("D-small-attempt0.in.txt", "r")

input = [[int(x) for x in row.strip().split(" ")] for row in file][1:]


for i, a in enumerate(input):
	x = pow(a[0], a[1] - 1)
	b = [str(1 + l * x) for l in range(0, a[0])]
	print "Case #" + str(i + 1) + ": " + " ".join(b)
