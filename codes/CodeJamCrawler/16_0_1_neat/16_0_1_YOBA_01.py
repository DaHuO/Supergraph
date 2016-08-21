import itertools


for t in range(int(input())):

    n = int(input())
    if n:

        s = set()
        for i in itertools.count(start=1):

            s |= set(map(int, str(i * n)))
            if s == set(range(10)):

                result = i * n
                break

    else:

        result = "INSOMNIA"

    print(str.format("Case #{}: {}", t + 1, result))
