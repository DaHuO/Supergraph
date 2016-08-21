if __name__ == '__main__':
    T = int(raw_input())

    for i in range(T):
        K, C, S = map(int, raw_input().split())
        ans = [str(j+1) for j in range(S)]
        print 'Case #%d: %s' % (i+1, ' '.join(ans))