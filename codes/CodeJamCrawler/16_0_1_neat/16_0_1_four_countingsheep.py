from collections import defaultdict

def main():
    with open("2countingsheep.txt") as data:
        counter = 1
        cases = data.readline()
        for rows in data.readlines():
            print("Case #{}: {}".format(counter, sheep(int(rows))))
            counter += 1


def sheep(N):
    if N == 0:
        return "INSOMNIA"
    seen = {}
    token = str(N)
    counter = 2
    for i in token:
        seen[i] = 1
    while sum(seen.values()) != 10:
        n = N*counter
        counter += 1
        for i in str(n):
            seen[i] = 1
    return n

main()
