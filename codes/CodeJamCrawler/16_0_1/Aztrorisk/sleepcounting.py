from Library import *
import math

def solve(n):
	if (n == 0):
		return "INSOMNIA";
	else:
		i = [False, False, False, False, False, False, False, False, False, False];
		j = 0;
		firstn = n;
		s = 1;
		while (j < 10):
			k = n % 10;
			if (i[k] == False):
				i[k] = True;
				j+=1;
				if (j == 10):
					return firstn * s;
			n = int(n / 10)
			if (n == 0):
				s+=1;
				n = firstn * s;


lines = getLines("A-large.in")
out = []

for i in range(int(lines[0])):
	value = int(lines[i + 1])
	res = solve(value)
	out.append("Case #%d: %s"%(i + 1, res))

writeOutLines("out.txt", out)