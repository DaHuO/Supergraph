
def count(num):
	if (num == num*2):
		return 'INSOMNIA'
	remaining = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
	mult = 1
	while 1:
		nextNum = str(num * mult)
		digits = set([int(i) for i in nextNum])
		remaining = remaining - digits
		if (len(remaining) == 0):
			return nextNum
		mult += 1

def main():
	fname = input()
	with open(fname) as f:
		with open('out.txt', 'w') as w:
			lines = f.readlines()
			i = 1
			for line in lines[1:]:
				w.write("Case #%i: %s\n" % (i, count(int(line))))
				i += 1


main()