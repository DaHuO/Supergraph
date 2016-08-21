import random
from math import sqrt

def mrange(start, stop, step):
    while start < stop:
        yield start
        start += step

def is_prime(num):
    return not any(num % i == 0 for i in mrange(3, int(sqrt(num)) + 1, 2))

def random_divisor(n):
    for i in mrange(2, n + 1, 1):
        if n % i == 0 and n != i:
            break
    return i

def random_binary(n):
    mx = (2 ** n) - 1
    b = bin(random.randint(0, mx))
    return b[2:].rjust(n, '0')

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n, j = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case

    # start solution
    coinjam_dict = {}

    while len(coinjam_dict) != j:
        is_coinjam = True
        list_of_bases = []

        # need n-2 digits since we know coinjams always start and end with 1
        mid_binary = random_binary(n-2)
        proposed_coinjam = '1{}1'.format(mid_binary)

        for base in range(2,11):
            based_proposed_coinjam = int(proposed_coinjam, base)
            list_of_bases.append(based_proposed_coinjam)
            if is_prime(based_proposed_coinjam):
                is_coinjam = False
        if is_coinjam and proposed_coinjam not in coinjam_dict:
            coinjam_dict[proposed_coinjam] = list_of_bases
    # end solution

    print("Case #{}:".format(i))
    for each_coinjam in coinjam_dict:
        proof = " ".join(str(random_divisor(x)) for x in coinjam_dict[each_coinjam])
        print('{} {}'.format(each_coinjam, proof))
    # check out .format's specification for more formatting options
