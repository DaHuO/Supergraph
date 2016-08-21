t = int(input()) 
for w in range(1, t + 1):
    n = list(input())
    v = 0
    i = 0
    if "-" not in n:
        print("Case #{}: 0".format(w))
        continue
    while "-" in n:
        if len(n) == i:
            v += 1
            break
        elif n[i] == '-':
            i += 1
        elif i == 0:
            while n[i] != '-':
                n[i] == '-'
                i += 1
            v += 1
        else:
            for x in range(i + 1):
                if '-' not in n:
                    break
                else:          
                    n[x] = '+'
            v += 1
            i = 0
    print("Case #{}: {}".format(w, v))
