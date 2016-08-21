from sys import argv


primes = [2,3,5]

def add_prime():
    global primes
    cand = primes[-1]
    while True:
        cand += 2
        if getdiv(cand) == 0:
            primes.append(cand)
            return

def getdiv(num, maxlimit=100):
    limit = num**0.5
    i = 0
    while True:
        p = primes[i]
        if p > limit:
            return 0
        if maxlimit is not None and p > maxlimit:
            return 0
        if num%p == 0:
            return p
        if i == len(primes) - 1:
            add_prime()
        i += 1


def nextcand(n):
    nextplace = str(n)[::-1].find('0')
    nextnum = n + 10**nextplace
    while nextplace >= 2:
        nextplace -= 1
        nextnum -= 10**nextplace
    return nextnum

def tobase(num, base):
    digits = [c for c in str(num)[::-1]]
    return sum([base**i for i in xrange(len(digits)) if digits[i]=='1'])


def goodcoin(num):
    for base in xrange(10, 1, -1):
        if getdiv(tobase(num, base), 100) == 0:
            return False, []
    divs = [getdiv(tobase(num, base)) for base in xrange(2, 11)]
    return True, divs

if len(argv) >= 2:
    lines = open(argv[1]).readlines()
    numcases = int(lines[0])

    for i, case in enumerate(lines[1:]):
        n, j = map(int, case.split(' '))
        cand = 10**(n-1) + 1
        answers = []
        while len(answers) < j:
            isgood, divs = goodcoin(cand)
            if isgood:
                answers.append((cand, divs))
            cand = nextcand(cand)
        print 'Case #%d:' % (i+1)
        for a in answers:
            print '%s' % int(a[0]),
            for d in a[1]:
                print '%d' % d,
            print ''


# def getnext(nums):
    # for i in xrange(2, 11):
        # nums[i] += i


# for i, case in enumerate(lines[1:]):
    # n, j = map(int, case.split(' '))
    # nums = [0]*11
    # for base in xrange(2, 11):
        # nums[base] = base**n + 1
    # answers = []
    # while len(answers) < j:
        # divs = map(getdiv, nums[2:11])
        # if 0 not in divs:
            # print 'answer found'
            # answer = bin(nums[2])[2:]
            # answers.append((answer, divs[:]))
        # getnext(nums)
    # print 'Case #%d:' % (i+1)
    # for a in answers:
        # print '%s' % a[0],
        # for d in a[1]:
            # print '%d' % d,
        # print ''
