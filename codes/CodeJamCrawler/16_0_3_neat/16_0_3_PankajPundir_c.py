import sys
import math

in_file = sys.argv[1]
out_file = in_file + ".out"


def is_prime(num):
    for i in xrange(3, int(math.sqrt(num) + 1), 2):
        if not (num % i):
            return False
    return True


def find_divisor(num):
    for i in xrange(3, int(math.sqrt(num) + 1), 2):
        if not (num % i):
            return i

with open(in_file, "r") as fh, open(out_file, "w") as oh:
    t = int(fh.readline().replace("\n", ""))
    for k in xrange(t):
        n, x = map(int, fh.readline().replace("\n", "").split(" "))
        s = int("1" + "0"*(n-2) + "1", 2)
        os = "Case #%s:\n" % (k+1)
        while x:
            bs = "{0:b}".format(s)
            prime = False
            for e in xrange(2, 11):
                if is_prime(int(bs, e)):
                    prime = True
                    break

            if not prime:
                os += bs + " "
                for e in xrange(2, 11):
                    os += str(find_divisor(int(bs, e))) + " "
                os += "\n"
                x -= 1

            s += 2
        oh.write(os)
