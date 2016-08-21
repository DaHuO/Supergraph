from collections import defaultdict

def ok(lt, d):
    # print "ok? lt: %s, d: %s" % (lt, d)
    cts = defaultdict(int)
    for c in d:
        cts[c] += 1
    for c in d:
        if lt[c] < cts[c]:
            # print "NIE OK"
            return False
    # print "OK"
    return True

T = int(raw_input())

digits = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

def compute(lt, phone):
    # print "compute lt = %s, phone = %s" % (lt, phone)
    if sum(lt.values()) == 0:
        # print "sum(lt.values()) == 0, returning %s" % phone
        return phone
    pos = 0
    for d in digits:
        # print "phone %s, d: %s, lt: %s" % (phone, d, lt)
        if ok(lt, d):
            # print "%s ok" % d
            ltc = lt.copy()
            for c in d:
                ltc[c] -= 1
            res = compute(ltc, phone + [pos])
            if res:
                # print "returning %s" % res
                return res
            # else:
            #     print "continuing iteration..."
        pos += 1
    # print "couldn't find anything, returning..."
    return False
    # for (k,v) in lt.items():
    #     if v != 0:
    #         print "...false"
    #         return False
    # print "...phone %s" % phone
    # return phone


for i in range(T):
    S = list(raw_input())
    lt = defaultdict(int)
    for s in S:
        lt[s] += 1

    phone = compute(lt.copy(), [])

    print "Case #%d: %s" % (i + 1, "".join(map(str, phone)))


    # XSENSIXNIENVNSEEOI