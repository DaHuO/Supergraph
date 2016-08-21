with open("sample_input.in", "r") as inp:
    inputs = inp.readlines()


nb = int(inputs[0].strip())
for idx in range(nb):
    i = int(inputs[idx + 1].strip())
    k = i
    if i == 0:
        sol = "INSOMNIA"
    else:
        digits = set(str(i))

        while len(digits) < 10:
            k += i
            digits.update(set(str(k)))

        sol = str(k)

    print("Case #%d: %s" % (idx + 1, sol))