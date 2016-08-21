import sys


f = open(sys.argv[1])

lines = f.readlines()[1:]


def output(case, result):
    print "Case #%s: %s" % (case + 1, result)


def replace(s, chars):
    for c in chars:
        s = s.replace(c, '', 1)
    return s


for index, S in enumerate(lines):
    out = []
    S = S.strip()

    while len(S) > 0:
        if "Z" in S:
            S = replace(S, 'ZERO')
            out.append(0)
            continue
        if 'X' in S:
            S = replace(S, 'SIX')
            out.append(6)
            continue
        if 'W' in S:
            S = replace(S, 'TWO')
            out.append(2)
            continue
        if 'S' in S:
            S = replace(S, 'SEVEN')
            out.append(7)
            continue
        if 'V' in S:
            S = replace(S, 'FIVE')
            out.append(5)
            continue
        if 'F' in S:
            S = replace(S, 'FOUR')
            out.append(4)
            continue
        if 'R' in S:
            S = replace(S, 'THREE')
            out.append(3)
            continue
        if 'O' in S:
            S = replace(S, 'ONE')
            out.append(1)
            continue
        if 'T' in S:
            S = replace(S, 'EIGHT')
            out.append(8)
            continue
        if 'I' in S:
            S = replace(S, 'NINE')
            out.append(9)
            continue

    out.sort()

    out = map(str, out)
    output(index, "".join(out).strip())
