
import sys

def solve(s, i):
    if i >= len(chrcts):
        return None

    ns = removeChars(s, chrcts[i])
    if ns is not None:
        if ns == '':
            return str(i)
        res = solve(ns, i) 
        if res is not None:
            return str(i) + res

    return solve(s, i+1)
    
    
    
def removeChars(s, cts):
    for c in cts:
        for x in range(cts[c]):
            if c not in s:
                return None
            s = s.replace(c,'',1)
    return s
    
def ctchars(s):
    cts = {}
    for c in s:
        if c not in cts:
            cts[c] = 1
        else:
            cts[c] += 1
    return cts
nums = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'TEN']
chrcts = []
for n in nums:
    chrcts.append(ctchars(n))
if __name__=="__main__":
        with open(sys.argv[1], 'U') as infile:
            with open(sys.argv[1]+'.out', 'w') as outfile:
                ncases = int(infile.readline()) 
                for t in range(ncases):
                    res = solve(infile.readline().strip(), 0)
                    outfile.write("Case #" + str(t+1) + ": " + res +'\n')

