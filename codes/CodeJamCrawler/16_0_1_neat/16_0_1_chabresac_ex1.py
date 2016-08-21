

def parse(f):
    with open(f, 'r') as c:
        lines = c.readlines()
    lines = [int(line.strip()) for line in lines]
    return lines[1:]


def solve(i):
    if i == 0:
        return 'INSOMNIA'
    else:
        a = set()
        for n in range(1, 100):
            for digit in str(i*n):
                a.add(digit)
            if len(a) == 10:
                return str(i*n)
        return 'INSOMNIA'

if __name__ == "__main__":
    inputs = parse('A-large.in')
    print(inputs)
    with open('ans.txt', 'w') as ans:
        for ind, i in enumerate(inputs):
            ans.write('Case #%d: %s\n' % (ind+1, solve(i)))
