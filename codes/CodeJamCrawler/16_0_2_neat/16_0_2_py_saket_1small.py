import random
T = 0
num_flips = 0
FLIP = { '+' : '-', '-' : '+'}
FUNNY_FACE = '+'
PLANE_FACE = '-'

def flip(face):
	return FLIP[face]

def order(case_num, seq):
	global num_flips
	if not seq:
		print 'Case #%d: %d' % (case_num + 1, num_flips)
		num_flips = 0	
	elif seq[-1] == FUNNY_FACE:
		order(case_num, seq[: -1])
	elif seq[-1] == PLANE_FACE:
		seq = map(flip, seq)
		num_flips += 1
		order(case_num, seq)

T = input()
for case_num in range(T):
	seq = raw_input()
	order(case_num, list(seq))
