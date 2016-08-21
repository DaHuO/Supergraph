'''

Small dataset : S = K

If a G appears in the original sequence:
	if the first tile is G, the first tile of all subsequent sequences will be G.
	
	if the first tile is L, then the first K tiles of all subsequent sequences will be the original sequence,
		so the first K tiles will have a G
	
	therefore, the first K tiles have a G

If no G appears in the original sequence:
	all subsequent sequences are all Ls

therefore, a sequence has a G iff its first K tiles have a G.

'''


def small(original_length, complexity, students):
	if original_length != students:
		return "???"
	
	return ' '.join(str(i) for i in range(1,original_length+1))
	


n_cases = input()

for case in range(1, n_cases+1):
	k,c,s = map(int,raw_input().split(' '))
	print 'Case #%d:' % case,
	print small(k,c,s)