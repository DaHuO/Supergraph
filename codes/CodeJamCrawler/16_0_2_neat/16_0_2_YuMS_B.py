def solve(cakes):
    current = True
    ans = 0
    for now in reversed(cakes):
        if now != current:
            ans += 1
            current = now
    return ans

def main():
    T = input()
    for i in xrange(1, T + 1):
        line = raw_input()
        cakes = [x == '+' for x in line.strip()]
        print 'Case #{0}: {1}'.format(i, solve(cakes))

if __name__ == '__main__':
    main()
