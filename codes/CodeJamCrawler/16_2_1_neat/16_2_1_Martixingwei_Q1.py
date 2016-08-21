from collections import Counter
words = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

def contains(container, contained):
    return all(container[x] >= contained[x] for x in contained)
    
def solve(s, n=0):
    if len(s)==0:
        return ""
    if n>9:
        return None
    w = Counter(words[n])
    if contains(s, w):
        res = solve(s-w, n)
        if res==None:
            return solve(s, n+1)
        return str(n)+res
    else:
        return solve(s, n+1)
        

filename = "A-small-attempt1.in"
f = open(filename,"r")
fout = open(filename.replace(".in", ".out"), "w")
N = int(f.readline())
for i in range(N):
    s = f.readline().strip()
    res = solve(Counter(s))
    print("Case #{}:".format(i+1), res)
    print("Case #{}:".format(i+1), res,file=fout)
f.close()
fout.close()