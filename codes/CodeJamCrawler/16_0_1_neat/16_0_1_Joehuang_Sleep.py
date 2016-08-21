def split(N):
    re_list = set([])
    while N is not 0:
        S = N/10
        Y = N - 10* S
        re_list.add(Y)
        N = S
    return re_list

def sleep(N):
	if N == 0:
		return "INSOMNIA"
	not_visited = set(range(10))
	count = 0
	while not_visited:
		count = count + 1
		not_visited = not_visited.difference(split(N*count))
	return count * N



num_input = int(raw_input())  # read a line with a single integer
for i in xrange(1, num_input + 1):
    N = int(raw_input())
    out = sleep(N)
    print "Case #{}: {}".format(i, out)



