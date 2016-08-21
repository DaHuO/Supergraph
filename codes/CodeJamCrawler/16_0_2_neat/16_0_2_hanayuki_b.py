import sys

T = int(raw_input())

def flip(S, i):
	tmp = S[:i+1]
	#print i, tmp
	for j in range(i+1):
		p = tmp[-1-j]
		S[j] = '+' if p == '-' else '-'
	return S


for t in range(1, T+1):
	num = 0
	S = list(raw_input())

	for i in range(len(S)-1, -1, -1):
		if S[i] == '-':

			# flip top '+' first
			if S[0] == '+':
				flip(S, S.index('-')-1)
				num += 1

			S = flip(S, i)
			num += 1

		#print S

	print 'Case #%d: %d' % (t, num)
