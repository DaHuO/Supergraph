import random, os

def first_factor(n):
    for i in xrange(2, 1000):
        if n % i == 0:
            return i
    return None


def binify(st):
    return ''.join("{:08b}".format(ord(x)) for x in st)

def rand_bits(l):
    return binify(os.urandom(l / 8 + 1))[:l]

        
def solve(n, j):
    print "Case #1:"

    jamcoins = set()

    while len(jamcoins) < j:
        cur = "1" + rand_bits(n-2) + "1"

        if cur in jamcoins:
            continue

        sample_divs = [first_factor(int(cur, base)) for base in xrange(2, 11)]

        if all(sample_div is not None for sample_div in sample_divs):
            jamcoins.add(cur)
            print cur + " " + " ".join(str(sample_div) for sample_div in sample_divs)
            

solve(32, 500)
