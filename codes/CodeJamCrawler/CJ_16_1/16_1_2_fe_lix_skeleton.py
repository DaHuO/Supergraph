import time
# each number should be counted twice
# find the ones that aren't, then sort them
def stringify(l):
    res = []
    for item in l:
        res.append(str(item))
    return res

def intify(l):
    res = []
    for item in l:
        res.append(int(item))
    return res



def missing_line(a):
    d = set([])
    for row in rows:
        for h in row:
            if h in d:
                d.remove(h)
            else:
                d.add(h)

    return stringify(sorted(intify(d)))



f = open("input.txt", "r+")
lines = tuple(f)

with open("output.txt", "w+") as o:
    cases = lines[0]
    i = 1
    case_number = 1
    while i < len(lines):
        j = i + 1
        print lines[i]
        n = int(lines[i])
        rows = []
        while j <= i + 2 * n -1:
            rows.append(lines[j].split())
            j += 1
        answer = missing_line(rows)
        o.write("Case #%d: %s\n" % (case_number, " ".join(answer)))
        i = i + 2*n
        case_number += 1
