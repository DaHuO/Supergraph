from sys import stdin


def solve(input):
    flips = 0
    prev = input[0]
    for n in input[1:]:
        if n != prev:
            flips += 1
        prev = n
    return flips

if __name__ == '__main__':
    cases = int(stdin.readline())
    cnt = 1
    while cases:
        input = []
        for c in stdin.readline():
            if c == '+':
                input.append(True)
            elif c == '-':
                input.append(False)
        input.append(True)
        result = solve(input)
        print 'Case #%d: %d' % (cnt, result)
        cnt += 1
        cases -= 1
