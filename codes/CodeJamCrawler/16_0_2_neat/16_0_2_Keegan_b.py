import fileinput
import itertools

def flip_count(s):
    s = s.rstrip('+')
    return len(list(itertools.groupby(s)))

fin = fileinput.input()
N = int(next(fin))
for i in range(1, N + 1):
    s = next(fin).strip()
    print("Case #{}: {}".format(i, flip_count(s)))
