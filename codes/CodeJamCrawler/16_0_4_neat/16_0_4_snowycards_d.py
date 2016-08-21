import sys

if __name__ == '__main__':

	sys.stdin.readline()
	cases = 100
	for case in range(1, cases+1):

		vals = sys.stdin.readline().split(" ")
		vals = [int(x) for x in vals]
		K, C, S = tuple(vals)

		outstr = "Case #" + str(case) + ":"

		for i in range(0, K):
			num = 0

			for j in range(0, C):
				num = num * K + i

			outstr += " " + str(num + 1)

		print outstr

