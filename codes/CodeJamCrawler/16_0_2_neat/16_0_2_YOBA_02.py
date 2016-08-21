for t in range(int(input())):

    s = list(map(lambda ch: ch == "+", str.strip(input())))
    l = len(s)
    n = 0
    while True:

        left, right = 0, l - 1
        while left < l and s[left]:

            left += 1

        while right >= 0 and s[right]:

            right -= 1

        if right < 0:

            break

        else:

            for i in range(left):

                s[i] = not s[i]

            for i in range(right + 1):

                s[i] = not s[i]

            n += bool(left) + 1

    print(str.format("Case #{}: {}", t + 1, n))
