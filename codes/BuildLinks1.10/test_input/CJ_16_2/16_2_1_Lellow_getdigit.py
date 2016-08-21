fichierR = open("A-small-attempt1.in","r")
fichieW = open("A-small-attempt1.out","w+")

def countNumber(s):
    tab = [0]*26
    for i in s:
        tab[ord(i)-65]+=1

    tab2 = [0] * 10

    tab2[0] = tab[ord('Z')-65]
    tab[ord('Z')-65] = 0
    tab[ord('E')-65] = tab[ord('E')-65] - tab2[0]
    tab[ord('R')-65] = tab[ord('R')-65] - tab2[0]
    tab[ord('O')-65] = tab[ord('O')-65] - tab2[0]


    tab2[2] = tab[ord('W')-65]
    tab[ord('W')-65] = 0
    tab[ord('T')-65] = tab[ord('T')-65] - tab2[2]
    tab[ord('O')-65] = tab[ord('O')-65] - tab2[2]


    tab2[6] = tab[ord('X')-65]
    tab[ord('X')-65] = 0
    tab[ord('S')-65] = tab[ord('S')-65] - tab2[6]
    tab[ord('I')-65] = tab[ord('I')-65] - tab2[6]

    tab2[8] = tab[ord('G')-65]
    tab[ord('G')-65] = 0
    tab[ord('E')-65] = tab[ord('E')-65] - tab2[8]
    tab[ord('I')-65] = tab[ord('I')-65] - tab2[8]
    tab[ord('T')-65] = tab[ord('T')-65] - tab2[8]
    tab[ord('H')-65] = tab[ord('H')-65] - tab2[8]


    tab2[3] = tab[ord('T')-65]
    tab[ord('T')-65] = 0
    tab[ord('R')-65] = tab[ord('R')-65] - tab2[3]
    tab[ord('H')-65] = tab[ord('H')-65] - tab2[3]
    tab[ord('E')-65] = tab[ord('E')-65] - 2*tab2[3]

    tab2[4] = tab[ord('R')-65]
    tab[ord('R')-65] = 0
    tab[ord('O')-65] = tab[ord('O')-65] - tab2[4]
    tab[ord('U')-65] = tab[ord('U')-65] - tab2[4]
    tab[ord('F')-65] = tab[ord('F')-65] - tab2[4]

    tab2[5] = tab[ord('F')-65]
    tab[ord('F')-65] = 0
    tab[ord('I')-65] = tab[ord('I')-65] - tab2[5]
    tab[ord('V')-65] = tab[ord('V')-65] - tab2[5]
    tab[ord('E')-65] = tab[ord('E')-65] - tab2[5]


    tab2[7] = tab[ord('F')-65]
    tab[ord('V')-65] = 0
    tab[ord('S')-65] = tab[ord('S')-65] - tab2[7]
    tab[ord('N')-65] = tab[ord('N')-65] - tab2[7]
    tab[ord('E')-65] = tab[ord('E')-65] - 2*tab2[7]

    tab2[1] = tab[ord('O')-65]
    tab[ord('O')-65] = 0
    tab[ord('N')-65] = tab[ord('N')-65] - tab2[1]
    tab[ord('E')-65] = tab[ord('E')-65] - tab2[1]

    tab2[9] = tab[ord('N')-65]


    ret = ""

    for k in range(len(tab2)):
        for j in range(tab2[k]):
            ret = ret + str(k)

    return ret




def parser(fichierR,fichierW):
    k = int(fichierR.readline())
    print(k)
    for i in range(1,k+1):
        a = fichierR.readline().split()
        fichierW.write("CASE #")
        fichierW.write(str(i))
        fichierW.write(": ")
        fichierW.write(countNumber(a[0]))
        fichierW.write("\n")



parser(fichierR,fichieW)