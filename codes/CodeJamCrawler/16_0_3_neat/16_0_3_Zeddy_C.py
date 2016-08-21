from random import randint
import math

# from https://helloacm.com/fermat-prime-test-algorithm/
def powmod(a, b, n):
    if b == 1:
        return a % n
    r = powmod(a, b / 2, n)
    r = r * r % n
    if (b & 1) == 1: # odd number
        r = r * a % n
    return r


def probalPrime(n, s):
    if n <= 1:
        return False
    if n <= 3:
        return True
    for _ in xrange(s):
        a = randint(2, n - 1)
        if powmod(a, n - 1, n) != 1:
            return False
    return True
# end of from https://helloacm.com/fermat-prime-test-algorithm/


def factors(n):
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


def gen_nums(value):
    ret = []
    str_value = bin(value)[2:]
    for ii in range(2, 11):
        ret.append(int(str_value, ii))

    return ret


def check_nums(nums):
    for testnum in nums:
        if probalPrime(testnum, 5):
            return False
    return True


def find_factor(value):
    testnum = 2
    limit = math.sqrt(value)
    while True:
        if value % testnum == 0:
            return testnum
        else:
            testnum += 1
    if testnum > limit:
        raise RuntimeError('value is not prime')


if __name__ == "__main__":

    #fin = open('B-large.in', 'r')
    #fout = open('B-large.out', 'w')

    fin = open('C-small-attempt0.in', 'r')
    fout = open('C-small-attempt0.out', 'w')

    cases = int(fin.readline())
    print cases

    for t in range(0, cases):
        print "Case #:%d" % (t+1)
        fout.write("Case #" + str(t+1) + ":" + "\n")

        stuff = fin.readline().split()
        n = int(stuff[0])
        j = int(stuff[1])

        jamcoins = []
        coins_found = 0

        for i in range(2**(n-1) + 1, 2**n, 2):
            potcoin = gen_nums(i)
            if check_nums(potcoin):
                print "potcoin: " + str(potcoin)
                fout.write(bin(i)[2:] + ' ')
                for base_num in potcoin:
                    fac = find_factor(base_num)
                    fout.write(str(fac) + ' ')
                fout.write('\n')
                coins_found += 1

            if coins_found >= j:
                break

    fin.close()
    fout.close()