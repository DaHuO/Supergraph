from itertools import combinations

mapping = {2: 32769, 3: 14348908, 4: 1073741825, 5: 30517578126, 6: 470184984577, 7: 4747561509944, 8: 35184372088833,
           9: 205891132094650, 10: 1000000000000001}
positions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
divisors = {}


def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n % 2 == 0: return False
    if n < 9: return True
    if n % 3 == 0: return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0: return False
        if n % (f + 2) == 0: return False
        f += 6
    return True


def get_divisor(integer):
    for x in xrange(2, int(integer ** 0.5)):
        if integer % x == 0:
            return x
    return None


def check_if_valid(number):
    if not is_prime(number):
        div = get_divisor(number)
        if div:
            return div
    return None


t = int(raw_input())

for i in xrange(1, t + 1):
    num, p = [int(s) for s in raw_input().split(" ")]
    print "Case #1:"
    count = 0
    num -= 2
    while count < p:
        for j in xrange(1, num + 1):
            for m in combinations(positions, j):
                is_valid = None
                for i in xrange(2, 11):
                    starter = mapping[i]
                    for n in m:
                        starter += pow(i, n)
                    is_valid = check_if_valid(starter)
                    if is_valid:
                        divisors[i] = str(is_valid)
                    else:
                        break
                if is_valid:
                    string = ''
                    count += 1
                    for t in xrange(1, num + 1):
                        if t in m:
                            string = '1' + string
                        else:
                            string = '0' + string
                    print '1{}1'.format(string),
                    for divisor in xrange(2, 11):
                        print " " + divisors[divisor],
                    print
                if count == p:
                    break
            if count == p:
                break
