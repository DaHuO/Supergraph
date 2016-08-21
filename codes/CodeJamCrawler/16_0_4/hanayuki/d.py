import sys

T = int(raw_input())

for t in range(1, T+1):
	K,C,S = map(int, raw_input().split())

	print 'Case #%d:' % (t),

	if C == 1:
		if S < K:
			print 'IMPOSSIBLE'
		else:
			print ' '.join(map(str, range(1, K+1)))
		continue

	if K == S:
		print ' '.join(map(str, range(1, K+1)))
		continue



'''
Original sequence GGG: GGGGGGGGG
Original sequence GGL: GGGGGGGGL
Original sequence GLG: GGGGLGGGG
Original sequence GLL: GGGGLLGLL
Original sequence LGG: LGGGGGGGG
Original sequence LGL: LGLGGGLGL
Original sequence LLG: LLGLLGGGG
Original sequence LLL: LLLLLLLLL
'''