import fileinput, random
# We'd expect most random jamcoins to be composite with fairly common factors... shouldn't have to run
# an exhaustive search

# https://primes.utm.edu/lists/small/1000.txt
primes = [
      2,     3,     5,     7,    11,    13,    17,    19,    23,    29, 
     31,    37,    41,    43,    47,    53,    59,    61,    67,    71, 
     73,    79,    83,    89,    97,   101,   103,   107,   109,   113, 
#   127,   131,   137,   139,   149,   151,   157,   163,   167,   173, 
#   179,   181,   191,   193,   197,   199,   211,   223,   227,   229, 
#   233,   239,   241,   251,   257,   263,   269,   271,   277,   281, 
#   283,   293,   307,   311,   313,   317,   331,   337,   347,   349, 
#   353,   359,   367,   373,   379,   383,   389,   397,   401,   409, 
#   419,   421,   431,   433,   439,   443,   449,   457,   461,   463, 
#   467,   479,   487,   491,   499,   503,   509,   521,   523,   541, 
#   547,   557,   563,   569,   571,   577,   587,   593,   599,   601, 
#   607,   613,   617,   619,   631,   641,   643,   647,   653,   659, 
#   661,   673,   677,   683,   691,   701,   709,   719,   727,   733, 
#   739,   743,   751,   757,   761,   769,   773,   787,   797,   809, 
#   811,   821,   823,   827,   829,   839,   853,   857,   859,   863, 
#   877,   881,   883,   887,   907,   911,   919,   929,   937,   941
]

N, J = map(int, [l for l in fileinput.input()][1].strip().split())

randomCandidate = lambda N: [1 if (l == 0 or l == N-1) else random.randint(0, 1) for l in range(N)]

print "Case #1:"

jcs = {}
checked = set()
while len(jcs) < J:
    candidate = randomCandidate(N)
    cstring = "".join(map(str, candidate))
    if (cstring in checked): continue;
    divisors = []
    for b in range(2, 11):
        divisor = None
        for p in primes:
            rem = 0
            reductionCounts = 0
            for c in candidate:
                tmp = b * rem + c
                rem = tmp % p
                if (rem != tmp): reductionCounts += 1
            if rem == 0 and reductionCounts > 1:
                divisor = p
                break
        if (divisor == None): break
        divisors.append(p)
    checked.add(cstring)
    if (len(divisors) == 9):
        jcs[cstring] = divisors
for c in jcs:
    print c, " ".join(map(str, jcs[c]))

