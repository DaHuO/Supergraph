import sys

def digits(n):
    return set(str(n))

def test(n):
    # TODO: Read a test case and return the answer to print
    seen = set()
    next = n
    for i in range(1, 101):
        seen |= digits(next)
        if len(seen) == 10:
            return next
        next += n
    return 'INSOMNIA'

def main(n):
    ''' Read and perform n test cases. '''

    for i in range(n):
        answer = test(int(sys.stdin.readline()))
        print('Case #{}: {}'.format(i+1, answer))

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    main(n)
