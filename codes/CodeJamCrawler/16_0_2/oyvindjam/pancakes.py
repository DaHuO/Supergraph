import sys

sys.stdin.readline()
with open("output", "w") as f:
    for test_case, pancakes in enumerate(sys.stdin, 1):
        flips = 0
        current, *rest = list(pancakes.strip())

        for pancake in rest:
            if (current != pancake):
                flips += 1
            current = pancake

        if current == "-":
            flips += 1

        f.write("Case #%d: %d\n" % (test_case, flips))
