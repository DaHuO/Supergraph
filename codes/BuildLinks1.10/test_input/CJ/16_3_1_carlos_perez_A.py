import collections

for testCase in xrange(input()):
	N = input()
	P = map(int, raw_input().split())
	partyMembers = collections.Counter()
	totalPartyMembers = sum(P)
	evacuatedPartyMembers = 0
	
	for i, p in enumerate(P):
		partyMembers[chr(ord('A') + i)] = p

	solution = []
	while evacuatedPartyMembers < totalPartyMembers:
		mostCommon = partyMembers.most_common(2)

		if len(mostCommon) == 1:
			p1, c1 = mostCommon[0]
			e = min(2, c1)
			solution += [p1 * e]
			partyMembers[p1] -= e
		else:
			p1, c1 = mostCommon[0]
			p2, c2 = mostCommon[1]

			if c1 > c2:
				e = min(2, c1 - c2)
				solution += [p1 * e]
				partyMembers[p1] -= e
			elif (totalPartyMembers - evacuatedPartyMembers) % 2 == 1:
				solution += [p1]
				partyMembers[p1] -= 1
			else:
				solution += [p1 + p2]
				partyMembers[p1] -= 1
				partyMembers[p2] -= 1

		evacuatedPartyMembers += len(solution[-1])

	print 'Case #{}: {}'.format(testCase + 1, ' '.join(solution))