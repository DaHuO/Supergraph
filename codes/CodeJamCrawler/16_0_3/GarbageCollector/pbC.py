#!/usr/bin/env python

def find_div(n):
	i = 2
	i_max = 1000
	while i < int(n**0.5)+1 and i < i_max:
		if n%i == 0:
			return i
		i+=1
	return -1



def solve_case(fout, N, J):
	jc_found = 0
	
	i = 0
	while i < 2**(N-2):
		i2 = 2 * i + 1 + 2**(N-1)
		i+=1
		print i2
		is_jc = True
		divs = []

		for j in range(2, 11):				
			div = find_div(int(bin(i2)[2:], j))
			if div == -1:
				is_jc = False
				break
			divs.append(div)
		
#		print is_jc
		if not is_jc:
			continue
		
		jc_found += 1
		div_p = ""
		for j in divs:
			div_p += str(j) + " "
		fout.write("{} {}\n".format(bin(i2)[2:], div_p))

		mul = 2
		while i2*mul < 2**N and jc_found < J:
			if (i2*mul)%2 == 1:			
				fout.write("{} {}\n".format(bin(i2*mul)[2:], div_p))
				jc_found += 1
			mul += 1

		if jc_found == J:
			return
#		print bin(i2)[2:]
		 

def main(argv):

	fout_name = argv[1].split(".")[0] + ".out"
	fout = open(fout_name, "w")

	fin = open(argv[1])
	nb_cases = int(fin.readline())


	for case_no in range(1, nb_cases+1):
		
#		print "Case:", case_no
		line = fin.readline().strip().split(' ')
		# Have read all stuff for this case:
		fout.write("Case #{}:\n".format(case_no))
		solve_case(fout, int(line[0]), int(line[1]))

	fout.close()
	fin.close()
	

import sys
if __name__ == "__main__":
    main(sys.argv)
