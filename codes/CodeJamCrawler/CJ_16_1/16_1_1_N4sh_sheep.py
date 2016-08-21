import sys


def reorder(word):
    S = list(word)
    new = []
    for idx in range(1,len(S)):
        if S[idx] >= S[0]:
            tmp = S.pop(idx)
            S = [tmp] + S
    return "".join(S)

def inputDissect(s):
    lines = s.split("\n")
    inputCnt = int(lines.pop(0))
    for offset in xrange(inputCnt):
        y = reorder(lines[offset])
        print "Case #%d:" % (offset + 1), y


inputDissect(open(sys.argv[1], "r").read())
