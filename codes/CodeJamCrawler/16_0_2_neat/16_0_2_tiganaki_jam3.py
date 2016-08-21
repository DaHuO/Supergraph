f=open("input10.in","r")
file = open("pancakes.txt", "w")
T=int(f.readline())
if 1<=T and 100>=T:
    for k in range(T):
        S=f.readline()
        S=list(S)
        S.remove('\n')
        n=0
        for i in range(len(S)-1):
            if S[i]!=S[i+1]:
                n=n+1
        if S[-1]=="-":
            n=n+1
        file.write("Case #")
        file.write(str(k+1))
        file.write(": ")
        file.write(str(n))
        file.write("\n")