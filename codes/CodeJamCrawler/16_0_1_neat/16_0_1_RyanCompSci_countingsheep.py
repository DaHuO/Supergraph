# Solution to problem A. Counting Sheep of google code jam

COMPLETE = set("0123456789")

T = int(input()) # number of cases
for case in range(1, T + 1):
    #Taking case input
    N = int(input())

    if N == 0:  # Check for possibility
        print("Case #{}: INSOMNIA".format(case))
        continue

    i = 0
    currentN = N
    visited = set()
    while visited != COMPLETE:
        i += 1
        currentN = N * i
        visited = visited | set(str( currentN ))

    print("Case #{}: {}".format(case, currentN))
