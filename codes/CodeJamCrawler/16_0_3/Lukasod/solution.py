import math as m

#precomputed primes
primes = [
    2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,
    193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,
    409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,
    641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,
    881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997,1009,1013,1019,1021,1031,1033,1039,1049,1051,1061,1063,1069,1087,1091,1093,
    1097,1103,1109,1117,1123,1129,1151,1153,1163,1171,1181,1187,1193,1201,1213,1217,1223,1229,1231,1237,1249,1259,1277,1279,1283,1289,1291,1297,
    1301,1303,1307,1319,1321,1327,1361,1367,1373,1381,1399,1409,1423,1427,1429,1433,1439,1447,1451,1453,1459,1471,1481,1483,1487,1489,1493,1499,
    1511,1523,1531,1543,1549,1553,1559,1567,1571,1579,1583,1597,1601,1607,1609,1613,1619,1621,1627,1637,1657,1663,1667,1669,1693,1697,1699,1709,
    1721,1723,1733,1741,1747,1753,1759,1777,1783,1787,1789,1801,1811,1823,1831,1847,1861,1867,1871,1873,1877,1879,1889,1901,1907,1913,1931,1933,
    1949,1951,1973,1979,1987,1993,1997,1999,2003,2011,2017,2027,2029,2039,2053,2063,2069,2081,2083,2087,2089,2099,2111,2113,2129,2131,2137,2141,
    2143,2153,2161,2179,2203,2207,2213,2221,2237,2239,2243,2251,2267,2269,2273,2281,2287,2293,2297,2309,2311,2333,2339,2341,2347,2351,2357,2371
]
## START: Miller–Rabin primality test
import random
_mrpt_num_trials = 6 # number of bases to test
def is_probable_prime(n):
    assert n >= 2
    # special case 2
    if n == 2:
        return (True,-1)
    # ensure n is odd
    #if n % 2 == 0:
    #    return (False, 2)
    # write n-1 as 2**s * d
    # repeatedly try to divide n-1 by 2
    s = 0
    d = n-1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient
    assert(2**s * d == n-1)

    # test the base a to see whether it is a witness for the compositeness of n
    def try_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True # n is definitely composite

    for i in range(_mrpt_num_trials):
        a = random.randrange(2, n)
        if try_composite(a):
            print("here")
            return (False, a)

    return (True,-1) # no base tested showed n as composite
## END: Miller–Rabin primality test

def is_composite(n, arr):
    for i in range(len(arr)):
        if n % arr[i] == 0:
            divisor = arr[i]
            del arr[i]
            return (True, divisor)
    else:
        return (False, -1)

def confirm_all_composite(bitstring):
    divisors = []
    unused_potential = [i for i in primes]
    for base in range(2, 11):
        prob_coposite,divisor = is_composite( int(bitstring, base), unused_potential )
        if not prob_coposite:
            return (False,)
        else:
            divisors.append(divisor)
    return (True, divisors)

def solution(jamcoin_length, desired_count):
    jamcoin_divisor = [] #each element form (jamcoin string, divisor)
    for i in range(2**(jamcoin_length - 2), 2*2**(jamcoin_length - 2)):
        bitstring = '1' + bin(i)[3:] + '1'
        bool_tuple = confirm_all_composite(bitstring)
        if bool_tuple[0]:
            jamcoin_divisor.append( (bitstring, bool_tuple[1]) )
        if len(jamcoin_divisor) >= desired_count:
            return jamcoin_divisor

##Running is beyond this
T = int(input().strip())

for i in range(T):
    N, J = [int(i) for i in input().strip().split(" ")]
    print("Case #" + str(i+1) + ":")
    for i in solution(N, J):
        print( i[0], " ".join([str(j) for j in i[1]]) )
