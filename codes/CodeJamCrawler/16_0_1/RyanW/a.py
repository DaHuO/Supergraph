def last_number(n):
    if n is 0:
        return None

    digits_seen = set()
    multiplier = 0

    while len(digits_seen) < 10:
        multiplier += 1
        digits_seen.update(str(n * multiplier))

    return n * multiplier


def main():
    T = int(raw_input())
    for t in xrange(1, T+1):
        N = int(raw_input())
        print 'Case #{}: {}'.format(t, last_number(N) or 'INSOMNIA')


if __name__ == '__main__':
    main()
