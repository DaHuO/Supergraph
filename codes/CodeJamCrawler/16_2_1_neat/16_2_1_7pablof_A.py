num = {0:"ZERO", 1:"ONE", 2:"TWO", 3:"THREE", 4:"FOUR", 5:"FIVE", 6:"SIX", 7:"SEVEN", 8:"EIGHT", 9:"NINE"}

##f = open('A-small-attempt4.in')
f = open('A-large.in')
f2 = open('file.txt','w')
T = f.readline()
i = 0

for l in f:
    i += 1
    r = ""
    l = l.strip()
    for b in [0, 2, 4, 6, 8, 3, 7, 5, 1, 9]:
        toRet = len(l)
        for x in set(num[b]):
            toRet = min(toRet, int(l.count(x) / num[b].count(x)))
        for x in num[b]:
            l=l.replace(x, '', toRet)
        r += toRet*str(b)
    if(len(l)>0):
        print(i)
    print("Case #" + str(i) + ": " + ''.join(sorted(r)),file=f2)
f.close()
f2.close()
