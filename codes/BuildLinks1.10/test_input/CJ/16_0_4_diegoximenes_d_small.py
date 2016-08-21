import sys

t = int(raw_input())
for tc in range(1, t+1):
	sys.stdout.write("Case #" + str(tc) + ": ")
	
	k, c, s = map(int, raw_input().split())
	
	out = [1]
	for i in range(1, k): out.append(out[-1] + k**(c-1))
	
	sys.stdout.write(str(out[0]))	
	for x in out[1:]: sys.stdout.write(" " + str(x))
	sys.stdout.write("\n")

