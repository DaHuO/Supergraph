def solve(n):
    if n==0:
        return "INSOMNIA"
    s10 = set("0123456789")
    s = set(str(n))
    f = 2
    while s!=s10:
        s.update(set(str(f*n)))
        f += 1
        
    return (f-1)*n
            

#filespec = "e:/work/code_jam/p1_practise.txt"    
filespec = "d:/downloads/A-small-attempt0.in"
#f = open(filespec, 'r')
f = open(filespec, 'r')
out = open("e:/work/code_jam/out.txt", 'w')

T = int(f.readline())
for i in range(1, T+1):
    n = int(f.readline())
    
    sol = solve(n)
    s = "Case #%d: %s\n" %(i, sol)
    
    out.write(s)
    
f.close()
out.close()