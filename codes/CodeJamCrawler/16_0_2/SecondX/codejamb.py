
def get_diff_index(seq):
	last = None
	for i, x in enumerate(seq, start=0):
		if not last:
			last = x
		if not last == x:
			return i
def run(seq):
	count = 0
	length = len(seq)
	while not seq.count('+') == length:
		diff = get_diff_index(seq)
		if diff is None:
			seq = '+'*length
		elif not diff == length:
			seq = seq[diff]*diff + seq[diff:]
		count +=1
	return count

txt = ''
with open('B-large.in', 'r') as f:
	txt = f.read()
	txt = txt.split('\n')
	with open('b.out', 'w') as f:
		for test_case in range(1, int(txt.pop(0))+1):
			seq = txt.pop(0)
			f.write('Case #%d: %d\n'%(test_case, run(seq)))