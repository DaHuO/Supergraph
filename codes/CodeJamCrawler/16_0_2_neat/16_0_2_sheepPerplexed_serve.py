import sys


def main():
    with open(sys.argv[1], 'r') as f:
        f.next()
        for idx, l in enumerate(f, start=1):
            l = l.rstrip()
            print 'Case #{}: {}'.format(idx, serve(l))


def serve(s):
    switch_count = 0
    last = s[0]
    s = s[1:]
    for p in s:
        if p != last:
            switch_count += 1
        last = p
    return switch_count + (last == '-')


if __name__ == '__main__':
    main()
