from sys import argv

def flipSign(sign):
    return "-" if sign == "+" else "+"

def flip(pancakes, desired_char):
    pancakes = list(pancakes)
    cakeIdx = 0
    if pancakes.count(flipSign(desired_char)) == 0:
        if desired_char == '+':
            return 0
        else:
            return 1

    while cakeIdx < len(pancakes) and pancakes[0] == pancakes[cakeIdx]:
        cakeIdx +=1
    for cakeSignIdx in xrange(cakeIdx):
        pancakes[cakeSignIdx] = flipSign(pancakes[cakeSignIdx])
    return 1 + flip(pancakes,desired_char)


def numflips(h_s):
    last_char = h_s[-1]
    split_idx = -1
    while split_idx > -len(h_s) and h_s[split_idx] == last_char:
        split_idx -=1
    split_idx +=1
    return flip(h_s[:split_idx], last_char)

def inputDissect(s):
    lines = s.split("\n")
    inputCnt = int(lines.pop(0))
    for offset in xrange(inputCnt):
        y = numflips(lines[offset])
        print "Case #%d:" % (offset + 1), y


#inp = """12
#-
#-+
#+-
#+++
#--+-
#++++-+
#-+
#+-
#+++
#--+-
#----+
#+-+-+-+-+-+-+-+-------+-+
#+++++++++++++++++++++++-+
#-------------------------"""
inputDissect(open(argv[1],"r").read())
