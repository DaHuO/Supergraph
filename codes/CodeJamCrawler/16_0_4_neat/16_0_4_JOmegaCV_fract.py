num = input()
for i in range(num):
    k, c, s = map(int, raw_input().split())
    print 'Case #%i:' % (i + 1), ' '.join(map(str, range(1, k**c + 1, k**(c-1))))