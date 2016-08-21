import sys

all_digits = {i for i in range(10)}

for i, line in enumerate(sys.stdin):
    if i == 0:
        continue
    line = line.strip()

    collected = set()
    ok = False
    n = int(line)
    for j in range(1, 100000):
        collected |= {int(i) for i in str(j * n)}
        if collected == all_digits:
            ok = True
            print("Case #{}: {}".format(i, n*j))
            break
    if not ok:
        print("Case #{}: INSOMNIA".format(i))
