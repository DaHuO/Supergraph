def f(n):
    s, i = set(), 0
    if n == 0:
        return "INSOMNIA"
    while len(s) != 10:
        i += 1
        s |= set(str(i*n))
    return i*n

fname = input()
with open(fname, 'r') as file:
    n = int(file.readline())
    numbers = [int(file.readline()) for i in range(n)]
    with open(fname[:-2]+"out", 'w') as file2:
        file2.write("\n".join(["Case #{}: {}".format(i+1, f(numbers[i])) for i in range(n)]))
