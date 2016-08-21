import argparse
import codejam.maths as mth

def jamcoin_divisors(jamcoin):
    if len(jamcoin) < 2:
        return False

    if jamcoin[0] != "1" or jamcoin[-1] != "1":
        return False

    divisors = []
    val = 0
    for n in range(2,11):
        val = long(jamcoin, base=n)
        factors = mth.prime_factors(val)
        prime = len(factors) == 1
        #print "Base %s: jamcoin '%s' == %s, prime = %s" % (n, jamcoin, val, prime)
        if prime:
            return False

        divisors.append(factors[0])

    return divisors


def next_jamcoin(length = 16, prev_jamcoin = None):
    if length < 2:
        raise Exception("Jamcoins must be at least 2 chars long.")

    if not prev_jamcoin:
        prev_jamcoin = "1%s1" % ("0" * (length-2))
        divisors = jamcoin_divisors(prev_jamcoin)
        if divisors:
            return (prev_jamcoin, divisors)

    elif length != len(prev_jamcoin):
        raise Exception("Specified length does not match length of supplied jamcoin")

    jamcoin = prev_jamcoin

    fragment = jamcoin[1:-1]
    next_fragment = ("{0:0%sb}" % (length-2)).format(long(fragment, base=2) + 1)
    jamcoin = "1%s1" % next_fragment

    divisors = False
    while not divisors:
        #print "Old jamcoin: %s" % jamcoin

        fragment = jamcoin[1:-1]
        next_fragment = ("{0:0%sb}" % (length-2)).format(long(fragment, base=2) + 1)
        if len(next_fragment) != len(fragment):
            raise Exception("No further jamcoin candidates")
        jamcoin = "1%s1" % next_fragment

        #print "Candidate jamcoin: %s" % jamcoin
        divisors = jamcoin_divisors(jamcoin)

    print "Next jamcoin: %s (%s)" % (jamcoin, divisors)
    return (jamcoin, divisors)


def find_jamcoins(n, j):
    """n = length of jamcoin, j = number of jamcoins to find"""
    print "Tasked to find %s jamcoins of length %s" % (j, n)

    jamcoin = [None]
    jamcoins = []
    while len(jamcoins) < j:
        jamcoin = next_jamcoin(n, jamcoin[0])

        #print jamcoin
        jamcoins.append(jamcoin)
        print "Found jamcoin #%s: %s" % (len(jamcoins), jamcoin[0])

    return jamcoins


def process(infile):
    with open("results_jamcoins", "w") as out:
        with open(infile) as f:
            contents = f.read().splitlines()

            spec = long(contents[0])
            n, j = [long(x) for x in contents[1].split(" ")]

            out.write("Case #1:\n")

            result = find_jamcoins(n, j)

            print "SOLUTIONS FOUND: %s" % result

            for jamcoin, divisors in result:
                print jamcoin, divisors
                out.write("%s %s\n" % (jamcoin, " ".join([str(x) for x in divisors])))



if __name__ == "__main__":
    a = argparse.ArgumentParser()
    a.add_argument("infile", help="The file to process.")

    args = a.parse_args()
    process(args.infile)