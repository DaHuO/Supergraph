import sys

total = int(sys.stdin.readline().strip())
for a in range(total):
    a += 1
    n = int(sys.stdin.readline().strip())
    seen_numbers = set()
    seen_digits = set()
    i = 1
    while True:
        current = i * n
        i += 1
        seen_digits.update(str(current))
        if len(seen_digits) == 10:
            print("Case #{}: {}".format(a, current))
            break
        elif current in seen_numbers:
            print("Case #{}: INSOMNIA".format(a))
            break
        seen_numbers.add(current)
