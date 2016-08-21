def minFlips(stack):
	numFlips = 0
	prev = stack[0]
	for face in stack[1:]:
		if face != prev:
			numFlips += 1
		prev = face
	if stack[-1] == '-':
		numFlips += 1
	return numFlips

def main():
	fname = input()
	with open(fname) as f:
		with open('pancakes-out.txt', 'w') as w:
			lines = f.readlines()
			i = 1
			for line in lines[1:]:
				w.write("Case #%i: %s\n" % (i, minFlips(line.strip())))
				i += 1

main()