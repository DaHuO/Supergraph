def main():
	for TEST in xrange(1, int(raw_input())+1):
		N = int(raw_input())
		counts = map(int, raw_input().split())
		parties = [[counts[i], chr(ord('A')+i)] for i in xrange(len(counts))]

		print "Case #%d:" % (TEST),

		while 1:
			parties.sort(reverse=True)

			if len(parties) >= 3:
				A, B, C = parties[0], parties[1], parties[2]
			if len(parties) == 2:
				A, B, C = parties[0], parties[1], [-1, '']

			if A[0] == 0:
				break

			if A[0] > B[0] + 1:
				A[0] -= 2
				print A[1] + A[1],	# both from first
			elif A[0] > B[0]:
				if A[0] == 1 or B[0] > C[0]:
					A[0] -= 1
					print A[1], # just one
				else:
					A[0] -= 2
					print A[1] + A[1],	# both from first
			elif A[0] == B[0]:
				if B[0] > C[0]:
					A[0] -= 1
					B[0] -= 1
					print A[1] + B[1],	# one from each
				else:
					A[0] -= 1
					print A[1], # just one

		print

main()
