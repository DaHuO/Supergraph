from sys import stdin
from collections import Counter

def updateWord(c,letter,word):
    count = c[letter]
    if count > 0:
        for l in word:
            c[l] -=count
    return count
def solve(word):
    c = Counter(word)
    res = [0]*10
    res[0]=updateWord(c,'Z','ZERO')
    res[8]=updateWord(c,'G','EIGHT')
    res[3]=updateWord(c,'H','THREE')
    res[6]=updateWord(c,'X','SIX')
    res[7]=updateWord(c,'S','SEVEN')
    res[4]=updateWord(c,'U','FOUR')
    res[2]=updateWord(c,'T','TWO')
    res[5]=updateWord(c,'F','FIVE')
    res[1]=updateWord(c,'O','ONE')
    res[9]=updateWord(c,'I','NINE')
    for _,x in c.iteritems():
        assert x==0
    phone=[]
    for i,x in enumerate(res):
        phone += [str(i)]*x
    return ''.join(phone
                   )
for case in xrange(1,1+int(stdin.readline())):
    word = stdin.readline().strip()
    print "Case #%d: %s" % (case, solve(word))