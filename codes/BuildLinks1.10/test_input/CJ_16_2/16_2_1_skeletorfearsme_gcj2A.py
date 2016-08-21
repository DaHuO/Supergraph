with open("b.in") as f:
    content = f.readlines()
fo = open("out.txt", "wb")
for T in range(1,len(content)):
    Digits=[0]*10
    S=list(content[T])[:-1]
    Digits[0]=S.count("Z")
    for i in range(Digits[0]):
        for c in"ZERO":
            S[S.index(c)]="@"
    Digits[2]=S.count("W")
    for i in range(Digits[2]):
        for c in"TWO":
            S[S.index(c)]="@"
    Digits[4]=S.count("U")
    for i in range(Digits[4]):
        for c in"FOUR":
            S[S.index(c)]="@"
    Digits[6]=S.count("X")
    for i in range(Digits[6]):
        for c in"SIX":
            S[S.index(c)]="@"
    Digits[8]=S.count("G")
    for i in range(Digits[8]):
        for c in"EIGHT":
            S[S.index(c)]="@"
    Digits[5]=S.count("F")
    for i in range(Digits[5]):
        for c in"FIVE":
            S[S.index(c)]="@"
    Digits[7]=S.count("V")
    for i in range(Digits[7]):
        for c in"SEVEN":
            S[S.index(c)]="@"
    Digits[1]=S.count("O")
    for i in range(Digits[1]):
        for c in"ONE":
            S[S.index(c)]="@"
    Digits[9]=S.count("N")/2
    for i in range(Digits[9]):
        #print(S)
        for c in"NINE":
            S[S.index(c)]="@"
    Digits[3]=S.count("T")

    O=""
    for D in range(10):
        O+=str(D)*Digits[D]
    fo.write("Case #" + str(T) + ": " + O + "\n")
fo.close()
print "done"
    
    
    
    
    #print T, S, Digits

