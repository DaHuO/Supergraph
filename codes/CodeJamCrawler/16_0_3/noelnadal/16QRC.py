from random import randint

def base(s,b):
    r = 0
    p = 1
    for i in range(len(s)):
        r += int(s[i])*p
        p *= b
    return r

R = []
while len(R) < 500:
    s = "1"
    for i in range(30):
        s += str(randint(0,1))
    s += "1"
    T = ""
    for i in range(2,11):
        ok = 0
        n = base(s,i)
        for j in range(2,min(1+n//2,10000)):
            if n % j == 0:
                ok = 1
                T = T + str(j) + " "
                break
        if ok == 0:
            break
    if ok == 1:
        c = str(n) + " " + T
        R = R + [c]
        print(len(R))

f = open("output.txt","w")
f.write("Case #1:\n")
for k in range(500):
    f.write(str(R[k])+"\n")
f.close()
    
