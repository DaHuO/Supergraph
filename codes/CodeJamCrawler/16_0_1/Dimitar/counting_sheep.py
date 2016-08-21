from sys import stdin, stdout, stderr

def solve(n):
    if n == 0:
        return "INSOMNIA"
    seen = set(str(n))
    c = n
    while len(seen) < 10:
        c += n
        seen.update(str(c))

    return c


if __name__ == "__main__":
    T = int(stdin.readline().strip())
    for t in range(1, T + 1):
        N = int(stdin.readline().strip())
        ans = solve(N)
        stdout.write("Case #{0}: {1}\n".format(t, ans))

