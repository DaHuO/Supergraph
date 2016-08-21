

def solution(n):
    if n == 0:
        return 'INSOMNIA'
    alldigits = {0,1,2,3,4,5,6,7,8,9}
    digits = set()
    i = 1
    while True:
        nn = n * i
        digits.update(map(int, str(nn)))
        if not alldigits.difference(digits):
            return nn
        i += 1


def main():
    with open('p1.in', 'r') as f:
        lines = f.readlines()

    t = lines.pop(0)
    for i, line in enumerate(lines):
        n = int(line)
        nn = solution(n)
        print 'Case #{}: {}'.format(i+1, nn)


if __name__ == '__main__':
    main()
