fp = open("q1l.txt")
fw = open("q1a.txt", 'w')
t = int(fp.readline().strip())
for case in range(t):
    b = set()
    n = int(fp.readline().strip())
    for i in range(max(100, n)):
        if i == max(100, n) - 1:
            fw.write("Case #{0}: {1}\n".format(case+1, "INSOMNIA"))
        if i == 0:
            continue
        s = n * i
        b |= set(str(s))
        print(case, b)
        if {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}.issubset(b):
            fw.write("Case #{0}: {1}\n".format(case+1, s))
            break
    
