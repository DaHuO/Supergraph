from sys import stdout

primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173]
primes.extend( [179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281] )
primes.extend( [283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409] )
#primes.extend( [419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541] )
#primes.extend( [547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659] )
#primes.extend( [661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809] )

def get_divisor(N):
	for m in primes:
		if( m > N / 2 ): return -1;
		if( (N%m) == 0 ):
			return m
	return -1

def update_divisors(numstr,divisors,numbers):
	dv = -1
	for base in range( 2, 11 ):
		mynum = int(numstr,base)
		dv = get_divisor(mynum)
		if( dv == -1 ): return False
		divisors[base-2] = str(dv)
		numbers[base-2] = str(mynum)
	return True

def read_input():
	arr = [];
	f = open( "input.txt" )
	num = int(f.readline().rstrip( "\n" ).rstrip( "\r" ))
	for line in f:
		line = line.rstrip( "\n" ).rstrip("\r");
		arr.append(line)
	if( num != len(arr) ):
		print "ERROR IN INPUT! " + str(num) + "," + str(len(arr))
		return []
	return arr

def check_case(tup):
	temp = tup.split()
	N = int(temp[0])
	J = int(temp[1])
	Jleft = J
		
	numstr = "1" + "0" * (N-1)
	numstrmax = "1" * N
	current10 = int(numstr,2)-1;
	max10 = int(numstrmax,2);
	divisors = [None]*9
	numbers = [None]*9
	
	while( Jleft > 0 ):
		current10 += 2
		if( current10 > max10 ):
			print "NO SOLUTION FOUND"
			print "Missing: " + str(Jleft)
			return ""
		numstr = format(current10, 'b')
		if( not update_divisors(numstr,divisors,numbers) ):
			#print "skip"
			continue
		print numstr + " " + " ".join(divisors)
		#print "  ->" + ",".join(numbers)
		Jleft -= 1;
		
	
	
	current10 += 1;
	str2 = format(current10, 'b')
	return ""
	
input_arr = read_input()
n_cases = len(input_arr)
for i in range(n_cases):
	print "Case #" + str(i+1) + ":"
	result = check_case(input_arr[i])
	#print "Case #" + str(i+1) + ": " + result
	



