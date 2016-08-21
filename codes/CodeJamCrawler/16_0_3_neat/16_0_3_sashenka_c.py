

def solve_one(n, j):
    i = 2 ** (n / 2 - 1)
    for count in xrange(j):
        num = bin(i)[2:]
        yield num + ''.join(reversed(list(num)))
        i += 1


def main():
    with open('input.txt') as input:
        with open('output.txt', 'w') as out:
            t = int(input.readline())
            n, j = map(int, input.readline().split())
            out.write('Case #1:\n')
            for line in solve_one(n, j):
                out.write('{} 3 4 5 6 7 8 9 10 11\n'.format(line))

if __name__ == '__main__':
    main()