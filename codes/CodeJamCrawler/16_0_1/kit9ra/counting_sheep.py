f = open("in.txt", "r")
g = open("out.txt", "w")

t = int(f.readline())

for tc in range (1, t + 1):
    ans = f.readline()
    n = int(ans)
    
    if not int(ans):
        g.write("Case #{}: INSOMNIA\n".format(tc))
        continue
    d = {}
    while (True):
        for i in ans:
            if unicode(i).isnumeric(): d[i] = 1
        if len(d) == 10:
            break
        ans = str(int(ans) + n)
            
    g.write("Case #{}: {}\n".format(tc, ans))    

f.close()
g.close()
