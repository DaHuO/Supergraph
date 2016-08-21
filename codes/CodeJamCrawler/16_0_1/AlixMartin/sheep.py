
FILENAME = 'test.in'

def main():
    with open('test.out', 'w') as g:
        with open(FILENAME) as input:
            T = int(input.readline())
            for t in range(T):
                N = int(input.readline())
                answer = calc(N)
                answer_str = 'Case #{}: '.format(t+1) + str(answer)
                print(answer_str)
                g.write(answer_str)
                g.write('\n')


def process(seen, x):
    for ch in str(x):
        seen.add(ch)
    return seen


def calc(N):
    if N == 0:
        return "INSOMNIA"
    seen = set()
    x = N
    while True:
        before = set(seen)
        after = process(seen, x)

        if len(after) == 10:
            return x
        x += N
        seen = after
    return 0


main()