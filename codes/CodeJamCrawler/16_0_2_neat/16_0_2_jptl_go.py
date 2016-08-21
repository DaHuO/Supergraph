import sys

lines = []
for line in sys.stdin:
	lines.append(line.strip())

def next():
	return lines.pop(0)

def main():
	tc = int(next())
	for i in range(tc):
		print("Case #%d: "%(i+1)+str(foo(next())))


def foo(str):
	str = str.rstrip('+')
	if len(str) == 0:
		return 0
	str = str.replace('+', '0')
	str = str.replace('-', '+')
	str = str.replace('0', '-')
	return 1 + foo(str)

if __name__ == "__main__":
	main()