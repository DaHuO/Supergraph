import sys

cin = sys.stdin.readlines()

T = int(cin[0].strip())
for case in range(1, T+1):
    stack = cin[case].strip()
    flips = 0
    prev = None
    for pancake in stack:
        if prev != None and pancake != prev:
            flips += 1
        prev = pancake
    if prev == "-":
        flips += 1
    print("Case #{}: {}".format(case, flips))

