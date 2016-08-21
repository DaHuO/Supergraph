import sys
i = 0
def get_sheep_num(val):
	if val == 0:
		return "INSOMNIA"
	m = 1
	map_int = set([])
	while m > 0:
		s = val * m
		ints = [int(i) for i in str(s)]
		# print ints
		map_int = map_int.union(set(ints))
		# print map_int
		if len(map_int) == 10:
			return s
		m = m + 1

for line in sys.stdin:
    val = int(line)
    if i == 0:
    	i = 1
    	continue
    print "Case #"+str(i)+": "+str(get_sheep_num(val))
    i = i + 1