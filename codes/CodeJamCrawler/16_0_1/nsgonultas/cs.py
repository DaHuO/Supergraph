with open("A-large.in") as f:
    tests = int(f.readline())
    nums = map(int, f.readlines())

results = list()
digits = set((0, 1, 2, 3, 4, 5, 6, 7, 8, 9))

for num in nums:
    if num == 0:
        results.append("INSOMNIA")
        continue
    seensofar = set()
    j = 1
    last = num * j
    seensofar.update(map(int, list(str(last))))

    while(seensofar != digits):
        j += 1
        last = num * j
        seensofar.update(map(int, list(str(last))))

    results.append(last)

with open("A-large.out", "w") as f:
    for i in range(tests):
        f.write("Case #" + str(i + 1) + ": " + str(results[i]) + "\n")
