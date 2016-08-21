R = []
f = open("input.txt","r")
T = int(f.readline())
for k in range(T):
    s = str(f.readline().strip())
    n = len(s)
    i = 0
    r = 0
    while i < n and s[i] == '-':
        i += 1
    if i > 0:
        r += 1
    while i < n:
        while i < n and s[i] == '+':
            i += 1
        j = i
        while i < n and s[i] == "-":
            i += 1
        if j < i:
            r += 2
    R = R + [r]
            
f.close()
f = open("output.txt","w")
for k in range(T):
    f.write("Case #"+str(k+1)+": "+str(R[k])+"\n")
f.close()
