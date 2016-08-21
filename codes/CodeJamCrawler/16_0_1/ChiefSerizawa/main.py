import sys

def add_digits_to_set(n, s):
    while n != 0:
        s.add(n % 10)
        n //= 10
    return s

def find_stop(n):
    if n == 0:
        return 0
    digits_set = set()
    i = 1
    while len(digits_set) != 10:
        add_digits_to_set(n * i, digits_set)
        i += 1
    return n * (i - 1)

f      = open(sys.argv[1])
nb     = int(f.readline())
starts = list(map(int, f.readlines()))

for i, start in enumerate(starts):
    stop = find_stop(start)
    if stop:
        print("Case #%d: %d" % (i+1, stop))
    else:
        print("Case #%d: INSOMNIA" % (i+1))

