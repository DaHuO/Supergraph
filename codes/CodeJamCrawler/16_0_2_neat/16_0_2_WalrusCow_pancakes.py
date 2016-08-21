import sys

def invert(c):
    if c == '+':
        return '-'
    if c == '-':
        return '+'
    raise ValueError('Invalid c: {}'.format(c))

def test(stack):
    moves = 0
    while not all(s == '+' for s in stack):
        num_to_flip = 0
        while num_to_flip < len(stack) and stack[num_to_flip] == stack[0]:
            num_to_flip += 1

        stack = invert(stack[0]) * num_to_flip + stack[num_to_flip:]
        moves += 1
    return moves


def main(n):
    ''' Read and perform n test cases. '''

    for i in range(n):
        answer = test(sys.stdin.readline().strip())
        print('Case #{}: {}'.format(i+1, answer))

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    main(n)
