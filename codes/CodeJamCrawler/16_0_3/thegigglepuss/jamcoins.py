import sys

def test(num):
    for divisor in range(2, int(num**0.5)):
        if num % divisor == 0:
            return divisor
    return 0

def bases(base10):
    return [int(base10, 2), int(base10, 3), int(str(base10), 4), int(str(base10), 5), int(str(base10), 6),
            int(str(base10), 7), int(str(base10), 8), int(str(base10), 9), int(str(base10), 10)]

with open(sys.argv[1], 'r') as f:
    lines = int(f.readline())
    count = 1
    for line in f:
        print "Case #{}:".format(count)
        lines = line.split(' ')
        n = int(lines[0])
        j = int(lines[1])
        seed = 10 ** (n - 1) + 1
        base2 = int(str(seed), 2)
        solved = 0
        while solved < j:
            divisors = []
            baseses = bases('{0:b}'.format(base2))
            for val in bases('{0:b}'.format(base2)):
                result = test(val)
                if result != 0:
                    divisors.append(str(result))
                else:
                    break
            if len(divisors) == 9:
                print '{0:b} {1}'.format(base2, ' '.join(divisors))
                solved += 1
            base2 = base2 + 2
        count += 1

