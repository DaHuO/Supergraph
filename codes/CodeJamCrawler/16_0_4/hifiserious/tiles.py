def get_tile_try_fields (k, c, s):
	if (s < k): 
		return "IMPOSSIBLE"
	elif (k == 1):
		return 1
	elif (c == 1): 
		return " ".join(map(str, range(1, k+1)))
	else:
		return " ".join(map(str, range(2, k+1)))


t = int(raw_input()) 
for i in xrange(1, t + 1):
   k, c, s = [int(f) for f in raw_input().split(" ")]
   print "Case #{}:".format(i), get_tile_try_fields(k, c, s)

