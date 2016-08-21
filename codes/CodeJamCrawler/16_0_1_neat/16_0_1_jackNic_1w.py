for k in range(int(input())):
    bl = False
    L = []

    i = 0
    N = int(input())
    if (N == 0):
        print("Case #"+str(k+1)+": INSOMNIA")
    else:
        while (bl == False):
            aux = N*(i+1)
            cad = str(aux)
            for j in range(len(cad)):
              
                
                if((cad[j] == "0") or (cad[j] == "1") or (cad[j] == "2") or (cad[j] == "3") or (cad[j] == "4") or (cad[j] == "5") or (cad[j] == "6") or (cad[j] == "7") or (cad[j] == "8") or (cad[j] == "9")):

                    L.append(cad[j])
                    L.sort()
                    lnr = set(L)
                    if (len(lnr)==10):
                        print("Case #"+str(k+1)+": "+str(aux))
                        bl = True
                        break
                    


            i = i+1
