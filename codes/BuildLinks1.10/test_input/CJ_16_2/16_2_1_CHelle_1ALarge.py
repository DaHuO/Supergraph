file = open("1ALIn.in","r")
T = int(file.readline())
##import sys
##T = int(sys.stdin.readline())
n = ""
for j in range (0,T):
    S = file.readline()
##    S = sys.stdin.readline()
    z = 0
    o = 0
    w = 0
    h = 0
    u = 0
    f = 0
    x = 0
    s = 0
    g = 0
    i = 0
    for l in S:
        if l == "Z":
            z = z+1
        elif l == "O":
            o = o+1
        elif l == "W":
            w = w+1
        elif l == "H":
            h = h+1
        elif l == "U":
            u = u+1
        elif l == "F":
            f = f+1
        elif l == "X":
            x = x+1
        elif l == "S":
            s = s+1
        elif l == "G":
            g = g+1
        elif l == "I":
            i = i+1
    tele = "0"*z+"1"*(o-z-w-u)+"2"*w+"3"*(h-g)+"4"*u+"5"*(f-u)+"6"*x+"7"*(s-x)+"8"*g+"9"*(i-g-x-f+u)
    n = n+"Case #"+str(j+1)+": "+tele+"\n"
n = n.strip()
##print(n)
file.close()
file = open("1ALOut.txt","w")
file.write(n)
file.close()
