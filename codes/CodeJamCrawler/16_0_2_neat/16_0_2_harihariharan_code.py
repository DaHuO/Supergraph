def strip_trailing_values(stacked_cakes, value):
    current_index = len(stacked_cakes) - 1
    num_cakes_to_strip = 0
    while current_index >= 0:
        if stacked_cakes[current_index] == value:
            num_cakes_to_strip += 1
            current_index -= 1
        else:
            break
    return stacked_cakes[:len(stacked_cakes)-num_cakes_to_strip]

def complement(stacked_cakes):
    complement_values = ""
    for cake in stacked_cakes:
        if cake == '+':
            complement_values += '-'
        else:
            complement_values += '+'
    return complement_values

def memoize(f):
    cache = {}
    return lambda *args: cache[args] if args in cache else cache.update({args: f(*args)}) or cache[args]

@memoize
def find_num_flips(stacked_cakes):
    if len(stacked_cakes) == 0:
        return 0
    last_index = len(stacked_cakes) - 1
    if stacked_cakes[last_index] == '+':
        return find_num_flips(strip_trailing_values(stacked_cakes, '+'))
    else:
        return 1 + find_num_flips(complement(strip_trailing_values(stacked_cakes, '-')))



if __name__ == "__main__":
	N = input()
	result = []
	for i in xrange(N):
		x = raw_input()
		result.append(find_num_flips(x))
	for i in xrange(N):
		print "Case #"+str(i+1)+": "+str(result[i])
