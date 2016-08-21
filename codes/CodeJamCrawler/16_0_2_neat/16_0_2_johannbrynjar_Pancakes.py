import re

flipSet = {'-': 1, '+': 0}
def multiple_replace(text, adict):
    rx = re.compile('|'.join(map(re.escape, adict)))
    def one_xlat(match):
        return adict[match.group(0)]
    return rx.sub(one_xlat, text)

def swapPancakes(str):
    dic = { "+": "-", "-": "+"}
    return multiple_replace(str, dic)

def mergePancakes(str):
    str = re.sub('\++','+',re.sub('\-+','-',str))
    if str != '+':
        return str.rstrip('+')
    return str

def countFlip(str):
    str = mergePancakes(str)
    if str in flipSet:
        return flipSet[str]
    else:
        swap = swapPancakes(str)
        newCount = countFlip(swap)
        flipSet[swap] = newCount
        return 1 + flipSet[swap]

if __name__ == "__main__":
    numberOfCase = int(raw_input(''))
    for i in xrange(numberOfCase):
        pancakes = raw_input('')
        c = countFlip(pancakes)
        print 'Case #{0}: {1}'.format(i+1, str(c))
