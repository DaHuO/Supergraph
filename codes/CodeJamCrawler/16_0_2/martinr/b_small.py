

def flip(s):
    r = ''
    for c in s:
        r += '-' if c=='+' else '+'
        
    return r

def solve(S):
    if len(S)==0:
        return 0
    elif set(S) == set('-'):
        return 1
    elif set(S) == set('+'):
        return 0

    if S[-1]=='+':
        i=-2
        while S[i] == '+' :
            i -= 1
        return solve(S[:i+1])
    else:
        i=-1
        while S[i] == '-' :
            i -= 1
        return 1+solve(flip(S[:i+1]))
            

#filespec = "e:/work/code_jam/b_practise.txt"    
#filespec = "d:/downloads/B-small-attempt0.in"
filespec = "d:/downloads/B-large.in"
#filespec = "e:/work/code_jam/b_test.txt"    
f = open(filespec, 'r')
out = open("e:/work/code_jam/b_out.txt", 'w')

T = int(f.readline())
for i in range(1, T+1):
    S = f.readline().strip()
    
    sol = solve(S)
    s = "Case #%d: %s\n" %(i, sol)
    print s
    out.write(s)
    
f.close()
out.close()
