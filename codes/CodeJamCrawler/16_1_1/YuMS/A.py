def solve(S):
    ans = ''
    for l in S:
        if l + ans > ans + l:
            ans = l + ans
        else:
            ans = ans + l
    return ans

def main():
    T = input()
    for i in xrange(1, T + 1):
        S = raw_input()
        print 'Case #{0}: {1}'.format(i, solve(S))

if __name__ == '__main__':
    main()
