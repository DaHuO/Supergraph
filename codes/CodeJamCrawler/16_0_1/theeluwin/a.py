infile = open('a.in')
outfile = open('a.out', 'w')
indata = infile.read().split('\n')
T = int(indata[0])

def push(ds, n):
	for k in str(n):
		ds[k] = 1

def solve(n):
	if n == 0:
		return 'INSOMNIA'
	ds = {}
	r = 0
	nn = n
	while len(ds) < 10:
		push(ds, nn)
		r += 1
		nn += n
	return r * n

def main():
	for t in range(1, T + 1):
		r = solve(int(indata[t]))
		outfile.write("Case #{}: {}\n".format(t, r))
