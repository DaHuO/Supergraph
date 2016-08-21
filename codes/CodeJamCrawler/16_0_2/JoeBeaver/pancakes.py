filename = "B-large.in"

def analyze(cNum, case):
    effectiveCase = case[:case.rfind('-') + 1]

    if effectiveCase:
        flips = 1 + effectiveCase.count('+-') + effectiveCase.count('-+')
    else:
        flips = 0
    return "Case #%s: %s\n" % (cNum, flips)


with open(filename, 'r') as f, open('output.txt', 'w') as out:
    t = int(f.readline())
    for i in range(1, t + 1):
        out.write(analyze(i, f.readline()))



