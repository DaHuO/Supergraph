import sys

test_path = 'A-test.in'


def main(input_path=test_path):
    with open(input_path) as f:
        T = int(f.readline().strip())
        for t in range(T):
            N = int(f.readline().strip())
            print("Case #{0}: {1}".format(t + 1, solve(N)))


def solve(N):
    return bfi(N)


def bfi(N):
    seen = [False] * 10
    seen_sofar = 0
    prev_numbers = set()
    i = 1

    while seen_sofar < 10:
        num = i * N
        if num in prev_numbers:
            return 'INSOMNIA'
        prev_numbers.add(num)

        for e in decomp(num):
            if not seen[e]:
                seen[e] = True
                seen_sofar += 1

        if seen_sofar == 10:
            return num

        i += 1
        # print(i)


def decomp(num):
    while num > 0:
        yield num % 10
        num //= 10

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()

