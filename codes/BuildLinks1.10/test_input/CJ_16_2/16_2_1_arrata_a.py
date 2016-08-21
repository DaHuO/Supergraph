import sys

t = int(sys.stdin.readline())
keynum = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

answernum = {}
for x in range(len(keynum)):
    answernum[keynum[x]] = str(x)

keystring = {'Z':'ZERO', 'X': 'SIX', 'W': 'TWO', 'G': 'EIGHT', 'H': 'THREE',
'U': 'FOUR', 'O': 'ONE', 'I': 'NINE', 'S': "SEVEN", 'V': 'FIVE'}
keychar = ['Z', 'X', 'W', 'G', 'H', 'U', 'O', 'V', 'S', 'I']


def removeword(dic, word):
    check = True
    for x in word:
        if dic[x] >= 1:
            continue
        else:
            return False
    for x in word:
        dic[x] -= 1
    return True

for i in range(t):
    ret = 0
    code = sys.stdin.readline().strip()

    dic = {}
    for x in keynum:
        for y in x:
            dic[y] = 0
    for x in code:
        dic[x] += 1
    ret = []
    for x in keychar:
        while(removeword(dic, keystring[x])):
            ret.append(answernum[keystring[x]])

    ret.sort()
    print "Case #%d:" % (i + 1), "".join(ret)
