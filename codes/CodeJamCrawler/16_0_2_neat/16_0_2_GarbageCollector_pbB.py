#!/usr/bin/env python

def swap(pks, num):
	ret = ""	
	for c in reversed(pks[:num]):
		if c == '-':
			ret += '+'
		elif c == '+':
			ret += '-'
		else:
			assert False
	
	for c in pks[num:]:
		ret += c
	return ret


def solve_case(pks):
	it = 0	

	while True:
#		print pks
		bot_bank = pks.rfind('-')
#		print bot_bank	
		if bot_bank == -1:
			return it
		top_bank = pks.find('-')
#		print top_bank
		if top_bank == 0:
			pks = swap(pks, bot_bank + 1)		
		else:
			pks = swap(pks, top_bank)			
		it += 1

def main(argv):

	fout_name = argv[1].split(".")[0] + ".out"
	fout = open(fout_name, "w")

	fin = open(argv[1])
	nb_cases = int(fin.readline())


	for case_no in range(1, nb_cases+1):
		
#		print "Case:", case_no
		pks = fin.readline().strip()
		# Have read all stuff for this case:
		fout.write( "Case #{}: {}\n".format(case_no, solve_case(pks)))

	fout.close()
	fin.close()
	

import sys
if __name__ == "__main__":
    main(sys.argv)
