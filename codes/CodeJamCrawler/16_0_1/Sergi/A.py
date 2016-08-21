
def calcular(n,x):
    visto0 = False;
    visto1 = False;
    visto2 = False;
    visto3 = False;
    visto4 = False;
    visto5 = False;
    visto6 = False;
    visto7 = False;
    visto8 = False;
    visto9 = False;


    if(n==0):
        print("Case #"+str(x+1)+": INSOMNIA")
        return
    acum=1
    while (True):
        nNuev=long(n)*long(acum)
        cadN=str(nNuev)
        for i in range(len(cadN)):
            if (cadN[i]=='0'):
                visto0=True
            if (cadN[i] == '1'):
                visto1 = True
            if (cadN[i] == '2'):
                visto2 = True
            if (cadN[i] == '3'):
                visto3 = True
            if (cadN[i] == '4'):
                visto4 = True
            if (cadN[i] == '5'):
                visto5 = True
            if (cadN[i] == '6'):
                visto6 = True
            if (cadN[i] == '7'):
                visto7 = True
            if (cadN[i] == '8'):
                visto8 = True
            if (cadN[i] == '9'):
                visto9 = True
        if(visto0==True and visto1==True and visto2==True and visto3==True and visto4==True and visto5==True and visto6==True and visto7==True and visto8==True and visto9==True):
            print("Case #" + str(x + 1) + ": "+str(nNuev))
            return
        acum=acum+1

def main():
    t = int(input())
    for i in range(t):
        n=long(input())
        calcular(n,i)


main()