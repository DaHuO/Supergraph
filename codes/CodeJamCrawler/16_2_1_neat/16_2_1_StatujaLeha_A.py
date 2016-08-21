def memoize(function):
    cache = {}
    def decorated_function(*args):
        try:
            return cache[args]
        except KeyError:
            val = function(*args)
            cache[args] = val
            return val
    return decorated_function

def input(file):
    F = open(file, "r")
    T = int(F.readline())
    for i in range(T):
        yield (i + 1), F.readline().strip()

def solve(S):
    D = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    Letters = sorted(set("".join(D)))

    def atomize(s):
        return tuple([sum([1 for a in s if a == e]) for e in Letters])

    words = [atomize(w) for w in D]

    def can(R, w):
        r = tuple([R[i] - w[i] for i in range(len(Letters))])
        return all(e >= 0 for e in r), r

    def F(R):
        if len(set(R)) == 1 and 0 in R:
            return True, ""

        for i in range(10):
            flag, r = can(R, words[i])
            if flag:
                flag, r = F(r)
                if flag:
                    return True, str(i) + r

        return False, ""
    F = memoize(F)

    flag, r = F(atomize(S))
    return "".join(sorted(r))

out = open("A.out", "w")

#for (case, S) in input("Asample.in"):
for (case, S) in input("A-small-attempt0.in"):
#for (case, S) in input("A-large.in"):
#for (case, S) in input("A-small-practice.in"):
#for (case, S) in input("A-large-practice.in"):
    print("Case #%d: %s" % (case, solve(S)), file = out)