def solve(N):
    if not N:
        return 'INSOMNIA'
    used = set()
    counter = 0
    while len(used) < 10:
        counter += 1
        number = counter * N
        while number:
            used.add(number % 10)
            number /= 10
    return counter * N

def main():
    T = input()
    for i in xrange(1, T + 1):
        N = input()
        print 'Case #{0}: {1}'.format(i, solve(N))

if __name__ == '__main__':
    main()
