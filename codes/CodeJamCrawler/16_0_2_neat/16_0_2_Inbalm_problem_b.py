def pancake_flipper(pancakes, sign, iter):
	set_of_sides = set(list(pancakes))
	if len(set_of_sides) == 1:
		if not list(set_of_sides)[0] == sign:
			return iter
		else:
			return iter + 1
	left_to_flip = pancakes.rfind(sign) + 1
	new_pancakes = pancakes[:left_to_flip]
	return pancake_flipper(new_pancakes, str(1-int(sign)), iter + 1)
	
		

t = int(raw_input())  # read a line with a single integer
map = {}
for i in xrange(1, t + 1):
	map = {}
	pancakes = raw_input()
	pancakes = pancakes.replace("+", "1").replace("-","0")
	value = pancake_flipper(pancakes, "0", 0)
	print "Case #{}: {}".format(i, value)
