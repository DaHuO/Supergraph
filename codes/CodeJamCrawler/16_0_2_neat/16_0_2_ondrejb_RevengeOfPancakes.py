def answer(panc):
    numFlips = 0
    for e in range(len(panc)-1,-1,-1):
        if panc[e] == "-":
            if numFlips % 2 == 0:
                numFlips = numFlips + 1
        else:
            if numFlips % 2 == 1:
                numFlips = numFlips + 1
    return numFlips
             
f = open("C:\Users\Ondrej Bohdal\Downloads\\B-large.in","r")
out = open("C:\Users\Ondrej Bohdal\Downloads\\B-large.out","w")
t = int(f.readline())

e = 0
while e<t:
    out.write("Case #"+str(e+1)+": "+str(answer(f.readline()))+"\n")
    e = e + 1
f.close()
out.close()