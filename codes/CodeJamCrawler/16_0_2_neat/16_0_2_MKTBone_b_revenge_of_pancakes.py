import fileinput

cases = [line.rstrip('\n') + '+' for line in list(fileinput.input())[1:]]
for i, s in enumerate(cases):
    print("Case #{}: {}".format(i + 1, sum([int(s[x] != s[x + 1]) for x in range(len(s) - 1)])))
