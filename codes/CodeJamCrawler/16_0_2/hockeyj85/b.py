from sys import stdout

T = int(raw_input())

for t in range(T):
	stdout.write("Case #"+str(t+1)+": ")

	line = raw_input()
	last = "roflcopter"
	flips = 0
	for a in line:
		if a != last:
			flips += 1
		last = a
	
	if line[len(line) - 1] != '-':
		flips -= 1

	stdout.write(str(flips)+"\n")
