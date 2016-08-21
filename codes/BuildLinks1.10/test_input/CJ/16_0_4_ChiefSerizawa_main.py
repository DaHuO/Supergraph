import sys

f = open(sys.argv[1])
n = int(f.readline())
cases = f.readlines()

for idx, case in enumerate(cases):
    k, c, s = list(map(int, case.split(' ')))
    to_print = " ".join(list(map(str, list(range(1, k+1)))))
    print("Case #%d: %s" % (idx + 1, to_print))
