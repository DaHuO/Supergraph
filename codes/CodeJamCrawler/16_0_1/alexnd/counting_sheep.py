def last_number(first):
    if first == 0:
        return 'INSOMNIA'
    N = first
    res = str(N)
    current = 1
    seen_digits = set()
    target = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
    while seen_digits != target:
        res = str(N * current)
        for char in res:
            seen_digits.add(char)
        current += 1
    return res

def main():
    with open('/Users/alex/Downloads/A-large.in.txt', 'r') as f:
        nCases = int(f.readline())
        for n in range(nCases):
            first = int(f.readline())
            result = last_number(first)
            print 'Case #%s: %s' % (str(n+1), str(result))

if __name__ == '__main__':
    main()
