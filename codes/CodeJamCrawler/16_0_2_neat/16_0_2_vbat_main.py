from itertools import tee, izip

importResults = list()

while True:
    try:
        text = raw_input()
        if len(text.strip()) == 0:
            break
        else:
            importResults.append(text.strip())
    except EOFError:
        break


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return izip(a, b)

def makePancake(x):
    num_flips = 0
    for v, w in pairwise(x):
        if v!=w:
            num_flips += 1
    if x[-1] == '-':
        num_flips += 1
    return num_flips

for i in range(len(importResults)):
    if i == 0:
        pass # this corresponds to the number of items
    else:
        print "Case #{case_id}: {result}".format(case_id = i, result = makePancake(importResults[i]))



