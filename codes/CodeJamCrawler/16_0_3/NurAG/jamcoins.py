import sys
import itertools

MAX = 100
PROBLEM = 'jamcoins'

BASES = [2, 3, 4, 5, 6, 7, 8, 9, 10]


def get_factor(n):
    k = 3
    while k*k <= n:
        if n % k == 0:
            return k
        k += 2
    return None


def in_base(str, b):
    result = 0
    for i, d in enumerate(str[::-1]):
        result = result + int(d) * pow(b, i)
    return result


def jamcoins(n, j):
    jamcoins = []
    for c in itertools.product('01', repeat=(n-2)):
        coin = '1' + (''.join(c)) + '1'

        results = []
        for b in BASES:
            value = in_base(coin, b)
            factor = get_factor(value)

            if factor is None:
                break
            else:
                results.append(factor)

        if len(results) == len(BASES):
            jamcoins.append((coin, map(lambda x: str(x), results)))
            if len(jamcoins) >= j:
                return jamcoins
            continue
    return 0


def main():
    if len(sys.argv) == 1:
        print (PROBLEM + '.py usage: python ' + PROBLEM + '.py <test case> ')
        sys.exit(-1)
    else:
        result = ''
        with open(sys.argv[1]) as f:
            lines = f.read().splitlines()
            num_tests = int(lines[0])
            tests = map(lambda x: x.split(), lines[1:num_tests + 1])

            for i, t in enumerate(tests):
                n = int(t[0])
                j = int(t[1])

                result = result + 'Case #' + str(i+1) + ': \n'

                for coins in jamcoins(n, j):
                    coin, coprimes = coins
                    result = result + coin + ' ' + ' '.join(coprimes) + '\n'
                if i + 1 < len(tests):
                    result = result + '\n'
        out = file('output-' + PROBLEM + '.out', 'w')
        out.write(result)
        out.close()


if __name__ == "__main__":
    main()
