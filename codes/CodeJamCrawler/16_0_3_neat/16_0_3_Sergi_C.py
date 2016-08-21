from math import sqrt

#Cambiar de base
def baseN(num,b,numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
    return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])

# Calculo lambda para sacar un binario de x tamanyo
get_bin = lambda x, n: format(x, 'b').zfill(n)

# Recibe a y b  y dvuelve el resto de dividirlos en la base
def restoBase(a,b,base):
    #print("a y b sin convertir "+str(a)+" "+str(b))
    b=baseN(b,base)

    #print("a y b convertidos " + str(a) + " " + str(b))

    z = int(str(b), base)
    y = int(str(a), base)
    '''while(y>z):
        y=int(str(a),base)
        y=y-z
        a=baseN(tmp,base)
    '''
    return y%z

def esPrimo(a):
    #print("Primo:"+str(a))

    if a < 2: return False,-1
    raiz=long(sqrt(float(a)))
    for x in range(2, raiz+1):
        #print("Pruebo a "+str(a) + " entre x "+str(x))
        resto=a%x
        if (resto == 0):
                return False,x
    return True,[-1]

#recibe un string n
def esValido(n):
    n=str(n)
    listaDiv=[]
    for i in range(2,11):
        tmp=long(n,i)

        #print("Vale " + str(tmp)+ " en base "+str(i))
        cond,div=esPrimo(tmp)
        if(cond==True):
            return [-1] # Caso fallido
        listaDiv.append(div)

    return listaDiv





def ampliarBin(n,j):
    while(len(n)<j):
        n="0"+str(n)
    return n


def calcular(n,j):
    print("Case #1:")
    numero=0
    while(True):
        binario=str(bin(numero))[2:]
        #print(binario)
        if(len(binario)>n-2):
            return
        binario=ampliarBin(binario,n-2)
        num=str("1")+str(binario)+str("1")
        #print("Compruebo "+str(num))
        lista=esValido(num)
        if(lista[0]!=-1):
            cadena=str(num)
            for i in range(len(lista)):
                cadena=cadena+" "+str(lista[i])
            print(cadena)
            j=j-1

        numero=numero+1
        if(j==0):
            return


t = int(input())
n,j = raw_input().split()
n = int(n)
j = int(j)
calcular(n,j)
#lista=esValido("110111")
#print(lista)
#lista=esValido("110011")
#print(lista)