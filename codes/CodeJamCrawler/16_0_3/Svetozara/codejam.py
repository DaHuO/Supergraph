import math
import random


def contains_any(str, str_set):
    """Check whether 'str' contains ANY of the chars in 'set'"""
    return 1 in [c in str for c in str_set]

#filename = input("Input name and location of input file: ")

primes_info = open("primes.txt", "r")
primes = []
for line in primes_info:
    line = line.rstrip('\n').strip(" ").replace("    "," ").replace("   ", " ").replace(" ", " ").replace("  ", " ")
    str_primes = line.split(' ')
    primes.extend([int(x) for x in str_primes])

problem = open("in.in", "r")

cases = int(problem.readline())

n, j = [int(s) for s in problem.readline().rstrip('\n').split(' ')]



#tests = []

#for i in range(cases):
#    tests.append(problem.readline().rstrip('\n'))

problem.close()

u_s = ""
l_s = ""

for i in range(n - 2):
    u_s += '1'
    l_s += '0'

u_s = '1' + u_s + '1'
l_s = '1' + l_s + '1'

lower_limit = int(l_s, base = 2)
upper_limit = int(u_s, base = 2)

candidates = [[] for i in range(j)]

check_candidates = set()

i = 0

bases = ['23456789', '3456789', '456789', '56789', '6789', '789', '89', '9', 'a']

while i < j:
    new_candidate = bin(random.randrange(lower_limit, upper_limit, 2))[2:]
    if new_candidate in check_candidates:
        continue
    check_candidates.add(new_candidate)
    divisors = []
    for base in range(2, 11):
        candidate = int(new_candidate, base = base)
        limit = math.floor(math.sqrt(candidate))
        for prime in primes:
            if prime > limit:
                break
            if candidate % prime == 0:
                divisors.append(str(prime))
                break
    if len(divisors) == 9:
        candidates[i].append(new_candidate)
        candidates[i].extend(divisors)
        print("found " + str(i))
        i += 1

output = "out.out"

out = open(output, "w")

out.write("Case #1:\n")

for candidate in candidates:
    s = ""
    for el in candidate:
        s += el + " "
    out.write(s.rstrip(" ") + "\n")

out.close()






#i = 1
#for test in tests:
#    out.write("Case #" + str(i) + ": ")
#    out.write(str(result(test)))
#    out.write("\n")
#    i += 1

#out.close()

