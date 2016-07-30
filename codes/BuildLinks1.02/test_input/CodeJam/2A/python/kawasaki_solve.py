from itertools import permutations

T = int(raw_input())
for tc in xrange(1, T + 1):
    N, R, P, S = map(int, raw_input().split())

    def solve():
        for hs in permutations('P' * P + 'R' * R + 'S' * S, r=1 << N):
            winners = hs
            for i in xrange(N):
                tmp = [None] * (len(winners) / 2)
                for j in xrange(1 << N - 1 - i):
                    tmp[j] = {
                        'RS': 'R',
                        'RP': 'P',
                        'SR': 'R',
                        'SP': 'S',
                        'PR': 'P',
                        'PS': 'S',
                    }.get(winners[2 * j] + winners[2 * j + 1])
                    if tmp[j] is None:
                        break
                else:
                    winners = tmp
                    continue
                break
            else:
                return ''.join(hs)
        return 'IMPOSSIBLE'

    print 'Case #{}: {}'.format(tc, solve())
