def Maneuver(s):
    n = len(s)
    
    res = 0
    i = 0
    while i < n:
        steps = 0
        while i < n and s[i] == "+":
            steps += 1
            i += 1
        if i == n:
            return res
        if steps:
            res += 1
        steps = 0
        while i < n and s[i] == "-":
            steps += 1
            i += 1
        if i == n:
            return res + 1
        if steps:
            res += 1
    return res
        
    


inf = open("in.txt", "r")
ouf = open("out.txt", "w")

for case in range(int(inf.readline())):
    n = inf.readline().strip()
    m = Maneuver(n)
    ouf.write("Case #" + str(case + 1) + ": " + str(m) + "\n")

inf.close()
ouf.close()