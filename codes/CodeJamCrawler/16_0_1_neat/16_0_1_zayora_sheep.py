tests = int(input())

results = []

for test in range(tests):
    n_str = input()
    n = int(n_str)
    i = 2

    if n == 0:
        results.append("Case #{}: {}".format(test+1, "INSOMNIA"))
        continue

    all_ten = set(range(10))
    s = set(map(int,n_str))

    while(s != all_ten):
        last_n = i*n
        s.update(set(map(int, str(last_n))))
        i += 1

    results.append("Case #{}: {}".format(test+1, last_n))

for result in results:
    print(result)
