
NUMS = ["ZERO", "ONE", "TWO", "THREE", "FOUR",
        "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

def contains(d1, d2):
    return all((k in d1 and v <= d1[k]) for k, v in d2.iteritems())
    
def sub(d1, d2):
    return {k: v - d2.get(k, 0) for k, v in d1.iteritems() if v != d2.get(k, 0)}
        
def extract(numsd, s, start):
    if s == {}:
        return []
    for i in xrange(start, len(numsd)):
        if contains(s, numsd[i]):
            res = extract(numsd, sub(s, numsd[i]), i)
            if res is not None:
                return [i] + res
    return None
        
        
import sys
f = sys.stdin
T = int(f.readline())
for case in xrange(1, T+1):
    s = f.readline().strip()
    sd = {c: s.count(c) for c in s}
    numsd = []
    for n in NUMS:
        numsd.append({c: n.count(c) for c in n})
    res = extract(numsd, sd, 0)
    print "Case #%d: %s" % (case, "".join(map(str,res)))
        