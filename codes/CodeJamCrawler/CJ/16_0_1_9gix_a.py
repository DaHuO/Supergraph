


def calculate(n):
    if n == 0:
        return 'INSOMNIA'
    initial_n = n
    remaining_digits = set(range(10))
    while len(remaining_digits) > 0:
        last_n = n
        currnum = {int(_) for _ in str(n)}
        remaining_digits -= currnum
        n = n + initial_n
    return last_n

def main():
    t = int(input())

    ts = []
    for i in range(t):
        n = int(input())
        ts.append(n)

    for i, n in enumerate(ts, 1):
        result = calculate(n)
        print("Case #{}: {}".format(i, result))

if __name__ == '__main__':
    main()