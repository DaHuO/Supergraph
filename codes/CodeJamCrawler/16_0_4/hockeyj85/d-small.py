from sys import stdout

T = int(raw_input())

for t in range(T):
	n = map(int, raw_input().split())[0]
	stdout.write("Case #"+str(t+1)+": ")
	stdout.write(str(1))
	for i in range(2, n + 1):
		stdout.write(" " + str(i))
	stdout.write("\n")

