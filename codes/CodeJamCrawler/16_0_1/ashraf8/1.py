#!/usr/bin/env python


def solv(n):

	i = 1;
	last = 0;
	d = [0] * 10;

	while True:
		res = i * n;
		# print "i = [%d] n = [%d] res = [%d] " % (i+1,n,res);
		if res == last: return "INSOMNIA";
		last = res;
		for j in str(res):
			d[int(j)] = 1;

		if sum(d) == 10: return res;
		i += 1;

def main():
	f = file("A-large.in","r");
	n = int(f.readline())
	for i in range(0,n):
		# print "solving " + str(i)
		print "Case #%d: %s" % (i+1,str(solv(int(f.readline()))))


if __name__ == "__main__":
	main()