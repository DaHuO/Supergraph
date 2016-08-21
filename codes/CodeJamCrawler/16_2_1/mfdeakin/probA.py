numTests = int(input())
for t in range(1, numTests + 1):
    s = input().strip().lower()
    cCount = {}
    for c in s:
        if c in cCount:
            cCount[c] += 1
        else:
            cCount[c] = 1
    uniques = {'z': ("zero", 0, 0), 'w': ("two", 2, 1), 'x': ("six", 6, 2),
               'g': ("eight", 8, 3), 'h': ("three", 3, 4), "u": ("four", 4, 5),
               'o': ("one", 1, 6), 'f': ("five", 5, 7), 'v': ("seven", 7, 8),
               'n': ("nine", 9, 9)}
    numCount = {}
    for i in sorted(uniques.keys(), key=lambda c: uniques[c][2]):
        while i in cCount and cCount[i] > 0:
            if uniques[i][1] in numCount:
                numCount[uniques[i][1]] += 1
            else:
                numCount[uniques[i][1]] = 1
            for c in uniques[i][0]:
                cCount[c] -= 1
    print("Case #" + str(t) + ": ", end="")
    for n in range(10):
        if n in numCount:
            for i in range(numCount[n]):
                print(str(n), end="")
    print()
