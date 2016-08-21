import sys

def readFile(fname):
	data = []
	with open(fname, 'r') as f:
		N = int(f.readline())
		print N
		for i in range(N):
			x = int(f.readline())
			data.append(x)
	return data


def process(data):
	out = []
	for x in data:
		temp = []
		buf = x
		if buf == 0:
			out.append('INSOMNIA')
		else:
			while len(temp) < 10:
				for c in str(buf):
					c = int(c)
					if c not in temp:
						temp.append(c)
				buf += x
			out.append(buf-x)
	return out

def output(fname, out):
	with open(fname, 'w') as f:
		for i, y in enumerate(out):
			f.write('Case #%d: %s\n' % (i+1, y))

if __name__ == '__main__':
	data = readFile(sys.argv[1])
	out = process(data)
	output(sys.argv[2], out)