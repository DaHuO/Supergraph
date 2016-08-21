t = int(raw_input())
for i in range(1, t + 1):
    s = raw_input().split()
    k = int(s[0])
    c = int(s[1])
    q = int(s[2])
    ret = 'Case #{}:'.format(i)
    for i in range(1, k + 1):
        ret += ' {}'.format(i)
    print ret