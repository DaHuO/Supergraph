def digits(n):
    seen = set()

    while n != 0:
        seen.add(n % 10)
        n /= 10

    return seen

def sheep(n):
    if n == 0:
        return "INSOMNIA"

    seen = set()

    for d in digits(n):
        seen.add(d)

    i = 1

    while True:
        if len(seen) == 10:
            return str(i * n)

        i += 1

        for d in digits(i * n):
            seen.add(d)

def main():
    t = int(raw_input())

    for case in range(1, t + 1):
        print("Case #" + str(case) + ": " + sheep(int(raw_input())))

main()

