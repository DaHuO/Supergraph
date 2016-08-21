words = ("ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE")
def f(j,i):
    d = {}
    d2 = {}
    for word in ("ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE")[j::i]:
        for ch in word:
            d.setdefault(ch, 0)
            d2.setdefault(ch, []).append(word)
            d[ch] += 1
    return {key:value[0] for key,value in d2.items() if len(value) == 1}
def doit(msg):
    d = {key:0 for key in 'QWERTYUIOPASDFGHJKLZXCVBNM'}
    for ch in msg:
        d.setdefault(ch, 0)
        d[ch] += 1
    t1 = f(0,1)
    t2 = f(1,2)
    #print t1, t2
    ans = [''] * 10
    for key, value in t1.items() + t2.items():
        if ans[words.index(value)]:
            continue
        ans[words.index(value)] = str(words.index(value)) * d[key]
        p = d[key]
        for ch in value:
            d[ch] -= p
        #print d
    ans[9] = '9' * d['I']
    return ''.join(ans)

n = int(raw_input())
for i in range(n):
    msg = raw_input()
    print "Case #%s: %s" % (i + 1, doit(msg))
        
