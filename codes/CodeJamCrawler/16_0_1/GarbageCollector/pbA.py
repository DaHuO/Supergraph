#!/usr/bin/env python

def fctand(a, b):
	return a and b

def solve_case(num_a):
	if num_a == 0:
		return "INSOMNIA"

	dicl = [False, False, False, False, False, False, False, False, False, False]

	i = 1
	num = num_a

	while True:
#		print "x"
		for c in str(num):
#			print c
			dicl[int(c)] = True
		
		if reduce(fctand, dicl):
			return num
		
		i += 1
		num = i * num_a			
				

def main(argv):

	fout_name = argv[1].split(".")[0] + ".out"
	fout = open(fout_name, "w")

	fin = open(argv[1])
	nb_cases = int(fin.readline())


	for case_no in range(1, nb_cases+1):
		
#		print "--", case_no

		init_num = int(fin.readline())
		# Have read all stuff for this case:
		fout.write( "Case #{}: {}\n".format(case_no, solve_case(init_num)))

	fout.close()
	fin.close()
	

import sys
if __name__ == "__main__":
    main(sys.argv)
