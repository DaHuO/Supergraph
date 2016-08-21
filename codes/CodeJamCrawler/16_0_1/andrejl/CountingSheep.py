for iteration in range(1, int(input()) + 1):
    n = int(input())

    if n == 0:
        print("Case #{0}: {1}".format(iteration, "INSOMNIA"))
        continue

    numbers = set(str(n))

    total = n
    while len(numbers) != 10:
        total += n
        numbers |= set(str(total))

    print("Case #{0}: {1}".format(iteration, total))
