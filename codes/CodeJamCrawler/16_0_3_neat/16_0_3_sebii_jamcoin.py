import random

random.seed()

def jamcoin(num):
    s = bin(num)[2:]

    divs = []
    for base in range(2, 11):
        n = int(s, base)
        x = 3
        while x * x <= n:
            if n % x == 0:
                divs.append(x)
                break
            x += 2

    if len(divs) == 9:
        return True, divs
    else:
        return False, []

def solve(N, J):
    max_range = 2 ** (N - 2) - 1
    to_add = 2 ** (N - 1)

    nums = set()
    found = []
    while len(found) < J:
        num = to_add + 2 * random.randint(0, max_range) + 1
        if num in nums:
            continue
        nums.add(num)
        jam, divs = jamcoin(num)
        if jam:
            found.append((bin(num), divs))

    return found

if __name__ == '__main__':
    sol = solve(16, 50)
    print 'Case #1:'
    for s in sol:
        print '{} {}'.format(s[0][2:], ' '.join(str(x) for x in s[1]))
