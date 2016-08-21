import sys

def main(): # s = k only
    n_cases = int(sys.stdin.readline()) # unused
    line_no = 0
    for line in sys.stdin:
        line_no += 1
        k, c, s = map(int, line.split())
        assert s == k, 'but you promised D:'
        total = k ** c
        block_size = total / s # = k ** (c-1)
        indices = map(lambda i: str(i*block_size + 1), range(s))
        print 'Case #{}: {}'.format(line_no, ' '.join(indices))


main()