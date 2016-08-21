from collections import defaultdict

if __name__ == "__main__":
	number_cases = int(raw_input())
	for j in xrange(number_cases):
		number_parties = int(raw_input())
		parties_members = [int(a) for a in raw_input().split(" ")]

		print "Case #%s: " % str(j+1),
		while 1:
			not_all_zero = False

			max1 = 0
			max2 = 0
			max1_party = -1
			max2_party = -1
			for i, party in enumerate(parties_members):

				if party > 0:
					not_all_zero = True

				if party > max1:
					max2 = max1
					max2_party = max1_party
					max1 = party
					max1_party = i
					if party - 1 > max2:
						max2 = party - 1
						max2_party = i


				elif party > max2:
					max2 = party
					max2_party = i


			if not not_all_zero:
				break 
			
			parties_members[max1_party] -= 1
			parties_members[max2_party] -= 1

			not_alone = False
			for party in parties_members:
				if party > 0 and not_alone:
					not_alone = False
					break

				if party > 0:
					not_alone = True

			if not_alone:
				parties_members[max2_party] += 1
				max2_party = -1


			if max2_party == -1:
				print "%s " % (chr(ord('A') + max1_party)),
			else:
				print "%s%s " % (chr(ord('A') + max1_party), chr(ord('A') + max2_party)),

		print ""




