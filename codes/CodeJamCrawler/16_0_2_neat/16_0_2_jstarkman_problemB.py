import sys
line_number = 0

def count_flips(stack):
	last = stack[0]
	count = 0
	for p in stack[1:]:
		if p != last:
			count += 1
		last = p
	if last == "-":
		count += 1
	return count
 
for line in sys.stdin:
	if line_number:
		flips = count_flips(line[:-1]) # trim \n
		print("Case #%d: %d" % (line_number, flips))
	line_number += 1
