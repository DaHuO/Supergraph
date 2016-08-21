

def solve_one(input):
    pancakes = input.readline().strip()
    count = 0
    prev = '+'
    for p in reversed(pancakes):
        if p != prev:
            prev = p
            count += 1
    return count


def main():
    with open('input.txt') as input:
        with open('output.txt', 'w') as out:
            t = int(input.readline())
            for case in xrange(t):
                out.write('Case #{}: {}\n'.format(case + 1, solve_one(input)))
                print case

if __name__ == '__main__':
    main()