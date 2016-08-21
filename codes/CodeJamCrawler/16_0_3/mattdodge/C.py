import math

def run_case(input):
    bits, to_generate = read_ints(input)
    jamcoins_generated = 0
    for i in range(2**(bits - 2)):
        jc = get_jamcoin(i, bits)
        divisors = get_jamcoin_divisors(jc)
        if divisors is not None:
            print("{} {}".format(jc, " ".join([str(d) for d in divisors])))
            jamcoins_generated += 1

        if jamcoins_generated >= to_generate:
            break
    return None


def get_jamcoin(num, bits):
    return "1" + "{0:b}".format(num).zfill(bits - 2) + "1"


def get_jamcoin_divisors(st):
    divisors = []
    for base in range(2, 11):
        divisor = get_divisor(int(st, base))
        if divisor is None:
            return None
        divisors.append(divisor)
    return divisors


def get_divisor(num):
    if num == 0 or num == 1:
        return None
    for x in range(2, math.ceil(math.sqrt(num))+1):
        if num % x == 0:
            return x
    else:
        return None

##############################
#    CODE JAM BOILERPLATE    #
##############################


def read_ints(input, n=1):
    """ Read n integers from input - all on one line, space separated """
    return (int(st) for st in read_strs(input, n))


def read_strs(input, n=1):
    """ Read n strings from input - all on one line, space separated """
    return input.pop(0).rstrip("\n").split(" ")

# GCJ boiler plate...call run_case for each case given
if __name__ == '__main__':
    import sys
    sys.setrecursionlimit(10000)
    lines = sys.stdin.readlines()
    sys.stdin = open('/dev/tty')
    num_cases = int(lines.pop(0))
    for case_num in range(num_cases):
        print("Case #%d: %s" % (case_num + 1, run_case(lines)))
