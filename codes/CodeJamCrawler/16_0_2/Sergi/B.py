from collections import deque

cola = deque([])

dic={}


def flip(n,x):
    #print("Recibo "+str(n)+ " con "+str(x))
    nueva=n[0:x+1]
    colita=n[x+1:]
    #print("La nueva es "+str(nueva)+ " y la colita "+colita)
    #Rotamos la nueva
    nuevaRot=nueva[::-1]
    #print("La nueva rotada es "+str(nuevaRot))

    nuevaRotInv=""
    for i in range(len(nuevaRot)):
        if(nuevaRot[i]=='+'):
            nuevaRotInv=nuevaRotInv+str("-")
        elif (nuevaRot[i]=='-'):
            nuevaRotInv = nuevaRotInv + str("+")
    #print("La nueva rotada invertida es "+str(nuevaRotInv))
    #print("Devolvemos"+nuevaRotInv+colita)

    return (nuevaRotInv+colita)

def generar():
    dic["+"]=0;
    cola.append("+")
    dic["++"]=0;
    cola.append("++")

    dic["+++"] = 0;
    cola.append("+++")

    dic["++++"] = 0;
    cola.append("++++")
    dic["+++++"] = 0;
    cola.append("+++++")
    dic["++++++"] = 0;
    cola.append("++++++")
    dic["+++++++"] = 0;
    cola.append("+++++++")
    dic["++++++++"] = 0;
    cola.append("++++++++")
    dic["+++++++++"] = 0;
    cola.append("+++++++++")
    dic["++++++++++"] = 0;
    cola.append("++++++++++")


    while cola:
        elemento=cola.popleft()
        valor=dic[elemento]
        #print("Elemento " + str(elemento) + " " + str(valor))
        for i in range(len(elemento)):

            tmp=flip(elemento,i)
            #print("Rotacion de " + elemento + " valor " + str(i)+ " resultado "+ tmp)

            if((tmp not in dic) or (dic[tmp]>(valor+1))):
            #    print("anyado "+str(tmp))
                dic[tmp]=valor+1
                cola.append(tmp)

generar()

#flip("++",0)
#flip("++",1)
#flip("++",2)

#flip("+-+-+-+-+-",0)
#flip("+-+-+-+-+-",1)
#flip("+-+-+-+-+-",2)
#flip("+-+-+-+-+-",3)

num=int(raw_input(''))
for i in range(num):
    linea=str(raw_input(''))
    print("Case #"+str(i+1)+": "+str(dic[linea]))
