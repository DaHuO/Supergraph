#!python
def remove_senator(senators):
    n = sum([1 if x > 0 else 0 for x in senators])
    m = max(senators)
    h = senators.count(m)
    x = senators.index(m)
    if n == 2 and h == 2:
        senators[x] -= 1
        y = senators.index(max(senators))
        senators[y] -= 1
        return [x,y]
    else:
        senators[x] -= 1
        return [x]


def to_abc(idx):
    return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[idx]


def solve(N, senators):
    res = []
    while sum(senators) > 0:
        idx = remove_senator(senators)
        res.append(''.join(map(to_abc, idx)))
    return ' '.join(res)


def main():
    n = int(raw_input())
    for c in range(1, n + 1):
        N = int(raw_input())
        senators = map(int, raw_input().split())
        res = solve(N, senators)
        print 'Case #%d: %s' % (c, res)
    
if __name__ == "__main__":
    main()
