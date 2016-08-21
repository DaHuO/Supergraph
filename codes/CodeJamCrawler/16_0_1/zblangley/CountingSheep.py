import sys

def count(n):
    if n == 0:
        return "INSOMNIA"

    seenCount = 0
    seen = [False] * 10

    current = n
    while seenCount < 10:
        for char in str(current):
            if not seen[int(char)]:
                seen[int(char)] = True
                seenCount += 1

        current += n

    return current - n

if __name__ == "__main__":
    numCases = int(input())

    for case in range(numCases):
        n = int(input())
        print("Case #{}: {}".format(case + 1, count(n)))
