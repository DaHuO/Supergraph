import sys

lines = []
for line in sys.stdin:
	lines.append(line.strip())

def next():
	return lines.pop(0)


def main():
	tc = int(next())
	for i in range(tc):
		print("Case #%d: "%(i+1)+str(foo(int(next()))))


def foo(n):
	if n == 0:
		return "INSOMNIA"

	seen = set()
	i = 1
	while True:
		for c in str(n*i):
			seen.add(c)
		if len(seen) == 10:
			return n*i 
		i += 1

main()
# print(foo(1692))
