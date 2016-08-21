with open("getting-digits-large-input.in.txt") as f:
	lines = f.readlines()

numTests = int(lines[0])

def getNumTypePivot (freq, pivots, others):
	sub = min([freq[p] for p in list(pivots)])
	print "others: ", others, " freq: ", freq, "sub: ", sub, "pivots: ", pivots
	for i in others:
		freq[i] = freq[i] - sub

	temp = sub
	for p in list(pivots):
		freq[p] -= sub

	return temp


ans = []
for t in range(0, numTests):
	print "Running test ", t
	letters = list(lines[t + 1])
	freq = {}
	for i in range(0, len(letters)):
		if letters[i] not in freq:
			freq[letters[i]] = 1
		else:
			freq[letters[i]] = freq[letters[i]] + 1

	# ONE
	# TWO
	# THREE
	# FOUR
	# FIVE
	# SIX
	# SEVEN
	# EIGHT
	# NINE

	res = ""
	pivots = ["Z", "X", "G", "W", "U", "FVI", "VS", "NI", "R"]  # Whatever remains must be one
	nums = ["ERO", "SI", "EIHT", "TO", "FOR", "E", "EEN", "NE", "THEE"]
	digits = ["0", "6", "8", "2", "4", "5", "7", "9", "3"]

	for i in range(0, len(pivots)):
		if all([freq.get(j, 0) > 0 for j in list(pivots[i])]):
			# We're good to go
			sub = getNumTypePivot(freq, pivots[i], nums[i])
			res += digits[i] * sub

	res += freq.get('O', 0) * "1"

	ans.append("Case #" + str(t + 1) + ": " + "".join(sorted(res)))
with open("getting-digits-large-out.out", "w") as f:
	f.write("\n".join(ans))
