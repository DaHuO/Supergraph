def is_non_prime(n):
    if n == 2:
        return 0
    if n == 3:
        return 0
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return i
        i += w
        w = 6 - w
    return 0


def check_and_prove(n):
    ans = []
    for i in range(2, 11):
        nr = int(str(n), i)
        q = is_non_prime(nr)
        if q:
            ans.append(q)
        else:
            return 0
    return ans


def solve(N, J):
    ans = []
    n = int('1' + '0' * (N-2) + '1')
    while len(ans) < J:
        c = check_and_prove(n)
        if c:
            ans.append([n] + c)
        n = int(str(bin(int(str(n), 2) + int('10', 2)))[2:])
    return ans


def main():
    f_in = open('C-small-attempt0.in', 'r')
    # f_in = open('C-small-test.in', 'r')
    f_out = open('C-small.out', 'w')

    _ = int(f_in.readline())
    N, J = [int(i) for i in f_in.readline().split()]
    f_out.write("Case #1:\n")
    s = solve(N, J)
    for i in s:
        f_out.write(' '.join([str(a) for a in i]) + '\n')
    f_in.close()
    f_out.close()

if __name__ == '__main__':
    main()
