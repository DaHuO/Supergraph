import sys

def solve(pan_cakes):
    cache = set()
    while pan_cakes:
        pan, moves = pan_cakes.pop(0)
        if all(pan):
            return moves
        for i in range(1, len(pan) + 1):
            l = [not(x) for x in reversed(pan[:i])] + pan[i:]
            h = str(l)
            if h not in cache:
                cache.add(h)
                pan_cakes.append((l, moves + 1))
    return -1

def run_test(case_number, generator):
    pan_cakes = [x == '+' for x in next(generator).strip()]
    moves = solve([(pan_cakes, 0)])
    print('Case #%d: %d' % (case_number, moves))

def main():
    generator = get_file()
    number_of_tests = int(next(generator))
    for test in range(1, number_of_tests + 1):
        run_test(test, generator)

def get_file():
    for line in sys.stdin:
        yield line
        
if __name__ == '__main__':
    main()