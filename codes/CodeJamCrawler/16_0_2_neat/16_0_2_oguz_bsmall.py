t = int(input())

for i in range(t):
    n = input()
    n_list = list(n[::-1])

    a = 0

    for b, e in enumerate(n_list):
        if e == "-":
            for j in range(b, len(n_list)):
                if n_list[j] == "-":
                    n_list[j] = "+"
                else:
                    n_list[j] = "-"

            a += 1

    print("Case #" + str(i + 1) + ": " + str(a))
