f_w = open('rez.txt', 'w')

def parse(a):
    i = 0
    while i < len(a) and a[i] == a[0]:
        i += 1
        
    if i == len(a):
        return ""
    
    return a[i:]
    
    

def solve(a, i):
    ans = 0
    if not '-' in a:
        print("Case #",i + 1, ": ", 0, file=f_w, sep="")
    else:
        while len(a) != 0 and '-' in a:
            a = parse(a)
            ans += 1
            
        print("Case #",i + 1, ": ", ans, file=f_w, sep="")
        
n = int(input())
for i in range(n):
    solve(input(), i)
    
f_w.close()