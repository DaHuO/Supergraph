
def get_primes(n):
    nums = range(2,n)
    primes = []
    for i in range(len(nums)):
        if nums[i] != -1:
            primes.append(nums[i])
            for j in range(i, len(nums), nums[i]):
                nums[j] = -1
    return primes


def get_base_n(binary, base):
    num = 0
    for i, b in enumerate(reversed(binary)):
        if b == '1':
            num += base**i
    return num


def is_jamcoin(binary):
    divisors = []
    print 'Checking %s' % ''.join(binary)
    for base in xrange(2, 11):
        curr_n = get_base_n(curr, base)
        for p in primes:
            if p >= curr_n:
                return False, []
            if curr_n % p == 0:
                divisors.append(str(p))
                print '\t Base %d: %d. Prime divisor: %d.' % (base, curr_n, p)
                break
    if len(divisors) < 9:
        return False, []
    return True, divisors


if __name__ == '__main__':
    primes = get_primes(10000)

    input = 'C-large.in'
    output = 'C-large.out'

    with open(input) as f:
        content = f.readlines()
    content = [x.strip('\n') for x in content]

    n, j = content[1].split(' ')
    n = int(n)
    j = int(j)

    startl = ['1'] + ['0']*(n-2) + ['1']
    startb = ''.join(startl)
    visited = set()
    visited.add(startb)
    bfs = [startb]
    solutions = 0

    with open(output, 'w') as o:
        o.write('Case #1:\n')
        while solutions < j and len(bfs) > 0:
            curr = list(bfs.pop(0))

            # Add all neighbors to bfs
            for i in xrange(1, len(curr)-1):
                # Flip a bit, append, and then flip back.
                curr[i] = '0' if curr[i] == '1' else '1'
                curr_s = ''.join(curr)
                if curr_s not in visited:
                    bfs.append(curr_s)
                    visited.add(curr_s)
                curr[i] = '0' if curr[i] == '1' else '1'

            is_jc, divisors = is_jamcoin(curr)
            if is_jc:
                o.write('%s %s' % (''.join(curr), ' '.join(divisors)))
                o.write('\n')
                solutions += 1
