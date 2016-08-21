

def solve_one(input):
    start, complexity, tests_count = map(int, input.readline().split())
    return ' '.join(map(str, range(1, start + 1)))


def main():
    with open('input.txt') as input:
        with open('output.txt', 'w') as out:
            t = int(input.readline())
            for case in xrange(t):
                out.write('Case #{}: {}\n'.format(case + 1, solve_one(input)))
                print case

if __name__ == '__main__':
    main()