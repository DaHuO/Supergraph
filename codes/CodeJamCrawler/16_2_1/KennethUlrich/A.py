import collections
import fileinput
import itertools

digits = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

freqs = [collections.Counter(s) for s in digits]

def solve(s, dgts):
    if not s:
        return dgts
    for e, d in enumerate(digits):
        t = s
        for c in d:
            if c in t:
                t = t.replace(c, "", 1)
            else:
                break
        else:
            result = solve(t, dgts + [e])
            if result is not None:
                return result
    return None


for e, line in enumerate(fileinput.input()):
    if fileinput.isfirstline():
        continue
    s = line.strip()
    #print s, c

    counts = solve(s, [])
    #print "counts", counts


    result = "".join(str(i) for i in counts)

    print "Case #{}: {}".format(e, result)
