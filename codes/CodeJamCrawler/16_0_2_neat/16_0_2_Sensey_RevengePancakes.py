__author__ = 'RAIZ'

def voltearTorre(torre):
    torre_out = []
    for i in torre:
        if i == "+":
            torre_out = torre_out + ["-"]
        else:
            torre_out = torre_out + ["+"]
    return torre_out

def maniobrar(torre_panqueques):
    if "-" not in torre_panqueques:
        return 0
    elif "+" not in torre_panqueques:
        return 1

    tp = list(torre_panqueques)
    maniobras = 0
    for i in range (1,len(tp)):
        if tp[i-1]!= tp[i]:
            tp = voltearTorre(tp[:i])+tp[i:]
            i = 1
            maniobras += 1
        #print(tp)

    if "+" not in tp:
        maniobras += 1

    return maniobras


#MAIN
numCasos = int(input())
for i in range(1, numCasos+1):
    torre_panqueques = input()

    response = maniobrar(torre_panqueques)

    print("Case #"+str(i)+": "+str(response))
quit()
