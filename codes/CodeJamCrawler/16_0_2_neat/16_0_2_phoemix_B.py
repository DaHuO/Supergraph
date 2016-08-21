t = int(raw_input())

for i in range(t):
	pancakes = raw_input()
	turns = 0
	current = pancakes[0]

	for next in pancakes[1:]:
		if current != next:
			turns += 1
		current = next

	if current == '-':
		turns += 1

	print "Case #%d: %d" %(i+1, turns)
