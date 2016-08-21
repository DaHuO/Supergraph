def count_sheep(n):
    if n == 0: # Special case? Not sure yet.
        return "INSOMNIA"
    seen = set()
    total = 0
    while len(seen) < 10:
        total += n
        seen |= set(str(total))
    return total

for case in range(int(input())):
    print("Case #{0}: {1}".format(case+1, count_sheep(int(input()))))
