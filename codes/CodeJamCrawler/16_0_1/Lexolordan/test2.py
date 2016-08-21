f_w = open('rez.txt', 'w')

def parse(a, b):
    while a != 0:
        b.add(a % 10)
        a //= 10
    

def solve(a, i):
    b = set()
    
    ans = 1
    if a == 0:
        print("Case #",i + 1, ": ", "INSOMNIA", file=f_w, sep="")
    else:
        while len(b) != 10:
            parse(ans * a, b)
            ans += 1
            
        print("Case #",i + 1, ": ", (ans - 1) * a, file=f_w, sep="")
        
n = int(input())
for i in range(n):
    solve(int(input()), i)
    
f_w.close()