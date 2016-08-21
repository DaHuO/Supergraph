def calculate(n):
    """
    >>> calculate(0)
    'INSOMNIA'
    >>> calculate(1)
    10
    >>> calculate(2)
    90
    >>> calculate(11)
    110
    >>> calculate(1692)
    5076
    """
    digitsPassed = set()
    numbersPassed = set()
    i = 1
    while len(digitsPassed) != 10 and i < 500:
        current = i * n
        if current in numbersPassed:
            return "INSOMNIA"

        for dig in str(current):
            digitsPassed.add(dig)

        numbersPassed.add(current)
        i += 1

    return (i - 1) * n


t = int(input())
for tI in range(0, t):
    n = int(input())
    print("Case  #{}: {}".format(tI + 1, calculate(n)))
