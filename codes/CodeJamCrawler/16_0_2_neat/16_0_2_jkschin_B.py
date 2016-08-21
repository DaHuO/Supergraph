
def write(out, case, answer):
	out.write("Case #%d: " %(case))
	out.write(str(answer) + "\n")

def parse(f):
	f = open(f, "r").read().split()
	n = f[0]
	return n, f[1:]

def opposite(c):
	if c=='-':
		return '+'
	return '-'

def flip(stack):
	prev = stack[0]
	ptr = 1
	end = False
	while (True):
		try:
			cur = stack[ptr]
			if cur != prev:
				break
		except IndexError:
			end = True
			break
		ptr += 1
	if end and prev=="+":
		return "All Flipped!"
	else:
		return opposite(prev)*ptr + stack[ptr:]
def main():	
	out = open("B-large.txt", "w")
	n, stacks = parse("B-large.in")
	n = int(n)
	for i in range(n):
		stack = stacks[i]
		print stack
		count = 0
		while True:
			stack = flip(stack)
			print stack
			if stack=="All Flipped!":
				break
			count += 1
		write(out, i+1, count)


main()