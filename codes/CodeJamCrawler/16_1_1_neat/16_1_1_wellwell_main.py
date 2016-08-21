f = open("input.txt", "r")
out = open("output.txt", "w")

tests = f.readline()

ss = f.read().split()

for test, s in enumerate(ss, start=1):
    out.write("Case #" + str(test) + ": ")

    res = s[0]

    for i in range(1, len(s)):
        a = res + s[i]
        b = s[i] + res
        if (a > b):
            res = a
        else:
            res = b

    out.write(res + "\n")
