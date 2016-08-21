invert = {"+":"-", "-":"+"}
def _reverse_find(st, ch):
	for i in range(len(st)-1, -1, -1):
		if st[i] == ch:
			return i
	return -1



def convert(st, to="+"):
	if st == "":
		return 0
	end = len(st) - 1
	count = 0
	while end > -1:
		st = st[:end+1]
		if st[-1] == to:
			end = _reverse_find(st, invert[to])
		else:
			end = _reverse_find(st, to)
			to = invert[to]
			count += 1
	return count

# print convert("+", "+")
# print convert("-", "+")
# print convert("-+", "+")
# print convert("+-", "+")
# print convert("+++--------", "+")
# print convert("--+-", "+")

T = int(raw_input())
count = 1
while count <= T:
	print "Case #%d: %d" % (count, convert(raw_input()))
	count += 1
