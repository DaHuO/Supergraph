import sys

line_number = 0;

for line in sys.stdin:
	if line_number:
		# each line: K C S
		(K,C,S) = line.split(" ")
		K = int(K); C = int(C); S = int(S);
		if S >= K: # True for all small inputs
			# check the first S tiles
			# if first tile is lead, will see entire original sequence
			# if first tile is gold, GOLD!
			s = str(list(range(1, K+1))).replace(",", "")[1:-1]
			print("Case #%d: %s" % (line_number, s))
	line_number += 1
