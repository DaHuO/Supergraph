
def count(x):
    c = [0 for _ in xrange(10)]
    while x != 0:
        c[x % 10] += 1
        x /= 10
    return c

def main():
    f = open('input.txt', 'r')
    fout = open('output.txt', 'w')
    T = int(f.readline())

    for i in xrange(T):
        n = int(f.readline())
        now = n
        c = count(now)
        b = False
        for j in xrange(1000):
            now += n
            flag = False
            for idx, k in enumerate(count(now)):
                c[idx] += k
                if c[idx] == 0:
                    flag = True
            if not flag:
                fout.write('Case #{}: {}\n'.format(i + 1, now))
                b = True
                break
        if not b:
            fout.write('Case #{}: INSOMNIA\n'.format(i + 1))
    fout.close()


if __name__ == "__main__":
    main()