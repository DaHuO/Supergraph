import sys

def add_digits(x, digits):
    while x > 0:
        digits.add(x%10)
        x /= 10


def solve(n, i):
    if n == 0:
        return "Case #%d: INSOMNIA" % (i+1)

    curr = 0
    digits = set()

    while len(digits) < 10:
        curr += n
        add_digits(curr, digits)

    return "Case #%d: %d" % (i+1, curr)


if __name__ == '__main__':
    input = 'A-large.in'
    output = 'A-large-soln.out'

    with open(input) as f:
        content = f.readlines()
    content = [x.strip('\n') for x in content]

    with open(output, 'w') as o:
        for i, c in enumerate(content[1:]):
            o.write(solve(int(c), i))
            o.write('\n')