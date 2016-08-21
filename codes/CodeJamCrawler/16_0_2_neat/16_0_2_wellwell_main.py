f = open("input.txt", "r")
out = open("output.txt", "w")

ss = f.read().split()[1:]

test = 1
for s in ss:
    s = s.rstrip("+")

    last = "?"
    count = 0
    for c in s:
        if c != last:
            count += 1

        last = c

    out.write("Case #{}: {}\n".format(test, count))
    test += 1
