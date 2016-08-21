n = {
    'P': ('PR', 'R'),
    'S': ('PS', 'P'),
    'R': ('RS', 'S'),
}

T = int(input())
for t in range(1, T + 1):
    N, R, P, S = map(int, input().split())
    anss = 'IMPOSSIBLE'
    for last in 'PRS':
        counter = {
            'P': 0,
            'R': 0,
            'S': 0,
        }
        counter[last] += 1
        ans = last
        while (counter['P'] <= P and counter['R'] <= R and counter['S'] <= S) and not (counter['P'] == P and counter['R'] == R and counter['S'] == S):
            next = ''
            for c in ans:
                nn, l = n[c]
                next += nn
                counter[l] += 1
            ans = next

        if counter['P'] == P and counter['R'] == R and counter['S'] == S:
            anss = ans
            break

    if anss != 'IMPOSSIBLE':
        a = 2
        while a < len(anss):
            b = a*2
            next = ''
            for i in range(0, len(anss), b):
                q = anss[i:i+a]
                w = anss[i+a:i+b]
                if q < w:
                    next += q+w
                else:
                    next += w+q

            anss = next
            a *= 2
    print('Case #%d: %s' % (t, anss))
