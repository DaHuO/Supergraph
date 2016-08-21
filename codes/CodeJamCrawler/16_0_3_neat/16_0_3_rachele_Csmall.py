import itertools
import time

output_file = "Clarge.out"

f_out = open(output_file, "w")

f_out.write("Case #1:\n")


N = 32
J = 500

primes_to_1000 = [2, 3,      5,      7,     11,     13,     17,     19,     23,     29, 
     31,     37,     41,     43,     47,     53,     59,     61,     67,     71, 
     73,     79,     83,     89,     97,    101,    103,    107,    109,   113, 
    127,    131,    137,    139,    149,    151,    157,    163,    167,    173, 
    179,    181,    191,    193,    197,    199,   211,    223,    227,    229, 
    233,    239,    241,    251,    257,    263,    269,    271,    277,    281, 
    283,    293,   307,     311,    313,    317,    331,    337,    347,    349, 
    353,    359,    367,    373,    379,   383,   389,    397,    401,    409, 
    419,    421,    431,    433,    439,    443,    449,    457,    461,    463, 
    467,    479,    487,    491,    499,    503,   509,    521,    523,    541, 
    547,    557,    563,    569,    571,    577,    587,    593,    599,    601, 
    607,    613,   617,    619,    631,    641,    643,    647,    653,    659, 
    661,    673,    677,    683,    691,    701,    709,    719,    727,    733, 
    739,    743,    751,    757,    761,    769,    773,    787,    797,    809, 
    811,    821,    823,    827,    829,    839,    853,    857,    859,    863, 
    877,    881,    883,    887,    907,   911,    919,    929,   937,    941, 
    947,    953,    967,    971,    977,    983,    991,    997]

l_primes = 168

perms = []
start = time.time()

for l in list(itertools.product([0,1], repeat=N-2-15)):
	p = "1000000000000000"
	for i in l:
		p += str(i)
	p+= "1"
	perms.append(p)

perms.sort()
print("Perms done...")

jamcoins = []
found = 0

for p in perms:
	print("p = " +str(p))
	jam = True
	j = [p]
	for b in range(2, 11):
		bp = int(str(p), b)
		# print("p in base " + str(b) + " = " + str(bp))
		is_prime = True
		for i in primes_to_1000:
			if bp % i == 0:
				is_prime  = False
				j.append(i)
				break
		if is_prime:
			jam = False
			break
	if jam:
		f_out.write(str(p) + " " + str(j[1]) + " " + str(j[2]) + " " + str(j[3]) + " " + str(j[4]) + " " + str(j[5]) + " " 
			+ str(j[6]) + " " + str(j[7]) + " " + str(j[8]) + " " + str(j[9]) + "\n")
		jamcoins.append(j)
		found+= 1
	if found == J:
		break

end = time.time()


print jamcoins
print len(jamcoins)
print(end-start)

f_out.close()




# for p in perms:
# 	print (p)