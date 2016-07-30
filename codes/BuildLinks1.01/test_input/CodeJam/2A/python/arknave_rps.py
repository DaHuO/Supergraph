def winner(a, b):
    if a > b:
        return winner(b, a)
    if a == 'P' and b == 'R':
        return 'P'
    if a == 'P' and b == 'S':
        return 'S'
    if a == 'R' and b == 'S':
        return 'R'

def valid(moves):
    while len(moves) > 1:
        n = ''
        for i in range(0, len(moves), 2):
            if moves[i] == moves[i + 1]:
                return False
            n += winner(moves[i], moves[i + 1])
        moves = n
    return True

def get_counts(p, r, s):
    counts = [(p, r, s)]
    while p + r + s > 1:
        p, s, r = (p + r - s) // 2, (p - r + s) // 2, (r - p + s) // 2
        counts.append((p, r, s))

    return counts

def solve(l, n):
    out = ''
    if l[0]:
        out = 'P'
    elif l[1]:
        out = 'R'
    else:
        out = 'S'

    for x in range(n):
        nx = ''
        for c in out:
            if c == 'P':
                nx += 'PR'
            elif c == 'R':
                nx += 'RS'
            else:
                nx += 'PS'
            if len(nx) & (len(nx) - 1) == 0:
                l = 1
                while l < len(nx):
                    a = -2 * l
                    b = -l
                    #print(l, nx, nx[:a], nx[a:b], nx[b:])
                    nx = nx[:a] + min(nx[a:], nx[b:] + nx[a:b])
                    l <<= 1
        out = nx

    return out

def main():
    T = int(input())
    for case_num in range(1, T + 1):
        n, r, p, s = map(int, input().split())
        works = True
        counts = get_counts(p, r, s)
        if any(any(v < 0 for v in row) for row in counts):
            print("Case #{}: IMPOSSIBLE".format(case_num))
        else:
            # a = PR, b = PS, c = RS
            print("Case #{}: {}".format(case_num, solve(counts[-1], n)))

main()
