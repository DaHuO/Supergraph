
L = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
dic2 = {'SEVEN': 7, 'NINE': 9, 'SIX': 6, 'THREE': 3, 'TWO': 2, 'FOUR': 4, 'ZERO': 0, 'FIVE': 5, 'EIGHT': 8, 'ONE': 1}
dic1 = {'E': ['ZERO', 'ONE', 'THREE', 'THREE', 'FIVE', 'SEVEN', 'SEVEN', 'EIGHT', 'NINE'], 'G': ['EIGHT'], 'F': ['FOUR', 'FIVE'], 'I': ['FIVE', 'SIX', 'EIGHT', 'NINE'], 'H': ['THREE', 'EIGHT'], 'O': ['ZERO', 'ONE', 'TWO', 'FOUR'], 'N': ['ONE', 'SEVEN', 'NINE', 'NINE'], 'S': ['SIX', 'SEVEN'], 'R': ['ZERO', 'THREE', 'FOUR'], 'U': ['FOUR'], 'T': ['TWO', 'THREE', 'EIGHT'], 'W': ['TWO'], 'V': ['FIVE', 'SEVEN'], 'X': ['SIX'], 'Z': ['ZERO']}

def build():
    dic = {}
    for s in L:
        for c in s:
            if c not in dic:
                dic[c] = []
            dic[c].append(s)
    return dic

def build_dic():
    c = 0
    dic = {}
    for s in L:
        dic[s] = c
        c+=1
    return dic

from collections import Counter

def t(s):
    return len(dic1[s])

def solve(input_):
    c = Counter(input_)
    res = []
    l = c.keys()
    l = sorted(l, key=t)
        
    for ch in l:
        while(c[ch]> 0):
            for s in dic1[ch]:
                f = True
                for i in s:
                    if i not in c:
                        f = False
                        break
                    else:
                        if c[i]< 1:
                            f = False
                            break
                if f:
                    res.append(dic2[s])
                    for i in s:
                        c[i]-= 1
                        if c[i] == 0:
                            c.pop(i)
                    break
            if len(c) == 0:
                break
    res.sort()
    return "".join([str(_) for _ in res])
        
                








if __name__ == "__main__":
##    test()
    testcases = input()
    for caseNr in xrange(1, testcases + 1):
        r_input = raw_input()
        res = solve(r_input)
        print("Case #%i: %s" % (caseNr, res))
