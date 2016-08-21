import itertools

D = {'+': '-',
     '-': '+'}


def flip(p, n):
    return ''.join([D[i] for i in p[:n][::-1]]) + p[n:]


def flip_l(p, l):
    for n in l:
        p = flip(p, n)
    return p


def solve(p):
    if p == '+' * len(p):
        return 0
    for n in range(1, len(p) + 10):
        gen = itertools.combinations_with_replacement(range(1, len(p)+1), n)
        for l in gen:
            if flip_l(p, l) == '+' * len(p):
                return n
    return -1


def main():
    f_in = open('B-small-attempt3.in', 'r')
    f_out = open('B-small.out', 'w')
    n = int(f_in.readline())
    for i in range(n):
        p = f_in.readline()
        s = "Case #{}: {}\n".format(i+1, solve(p.strip()))
        print s
        f_out.write(s)
    f_in.close()
    f_out.close()

if __name__ == '__main__':
    main()
