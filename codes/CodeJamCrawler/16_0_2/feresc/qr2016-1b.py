#!python
def solve(s, c):
    if not s:
        return c
    while s[-1] == 1:
        s.pop(-1)
        if not s:
            return c
    if len(s) == 1:
        return c + 1
    if len(set(s)) == 1:
        return c + 1
    fst = s[0]
    snd = s[1]
    cnt = 1
    while fst == snd:
        cnt += 1
        fst = snd
        snd = s[cnt]
    for i in range(cnt):
        s[i] = snd
    return solve(s,c+1)
    

def main():
    n = int(raw_input())
    for c in range(1, n + 1):
        s = map(lambda x: 1 if x=='+' else 0, raw_input())
        res = solve(s, 0)
        print 'Case #%d: %d' % (c, res)
    
if __name__ == "__main__":
  main()
    
