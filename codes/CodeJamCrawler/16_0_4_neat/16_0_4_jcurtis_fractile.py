def test():
    assert(solve(1, 1, 1) == [1])
    assert(solve(1, 2, 1) == [1])
    assert(solve(1, 99, 1) == [1])
    assert(solve(2, 1, 2) == [1, 2])
    assert(solve(2, 2, 2) == [1, 3])
    assert(solve(2, 3, 2) == [1, 5])
    assert(solve(2, 4, 2) == [1, 9])
    assert(solve(3, 1, 3) == [1, 2, 3])
    assert(solve(3, 2, 3) == [1, 4, 7])
    assert(solve(3, 3, 3) == [1, 10, 19])


def solve_small(k, c, s):
    start = range(k)
    gap = k**(c-1)
    tiles = map(lambda n : n * gap + 1, range(k))
    return tiles

def solve(k, c, s):
    if k == s:
        return solve_small(k, c, s)
    return []

if __name__ == '__main__':
    test()
    T = int(raw_input())
    for n in range(1, T+1):
        k, c, s =  map(int, raw_input().split(' '))
        tiles = solve(k, c, s)
        ans = 'IMPOSSIBLE'
        if len(tiles) > 0:
           ans = ' '.join(map(str, tiles))
           print 'Case #{}: {}'.format(n, ans)
