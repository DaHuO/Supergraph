
def get_to_flip(cakes):

	first = cakes[0]

	for i, cake in enumerate(cakes):
		if cake != first: return i

	return len(cakes)


def flip(cakes, to_flip):

	begin = list(cakes[:to_flip])
	end = list(cakes[to_flip:])
	begin = list(map(lambda x: '-' if x == '+' else '+', begin))
	begin.reverse()
	full = begin + end

	return ''.join(full)


infile = 'input.in'

lines = [line.rstrip('\n') for line in open(infile, 'r')]

T = int(lines[0])

for t in range(1, T + 1):

	cakes = lines[t]
	goal = '+'*len(cakes)
	flips = 0

	while cakes != goal:

		to_flip = get_to_flip(cakes) # to_flip = first index of the cake which must not be fliped
		cakes = flip(cakes, to_flip)
		flips += 1

	print('Case #{t}: {flips}'.format(t=t, flips=flips))