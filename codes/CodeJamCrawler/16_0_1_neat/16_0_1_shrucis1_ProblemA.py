def lastnum(N):
    remaining = ["0","1","2","3","4","5","6","7","8","9"]
    if(N==0):
        return "INSOMNIA"
    i = 1
    while True:
        a = str(N*i)
        for e in a:
            if e in remaining:
                remaining.remove(e)
        if(len(remaining)==0):
            return a
        i += 1
    
f = open(r"C:\Users\Neil\Downloads\A-large.in")
s = f.read().split("\n")
f.close()
t = int(s[0])
for j in range(t):
    print("Case #" + (str(j+1)) + ": " + lastnum(int(s[1+j])))

