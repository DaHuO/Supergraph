archivo=open("C-small-attempt3.in")


lineas=[]


for linea in archivo.readlines():


    lineas.append(linea.strip().split(" "))

def EsPrimo (n):
    a=2
    while a<=n**(0.5):
        if n%a==0:
            return a
        else:
            a+=1
    return False

def binario(longitud):
    numero=0
    for c in range (longitud):
        numero+=2**c
    return numero

def numeroabinario(numero, longitud):
    restos=[0]*longitud
    cociente=numero
    a=-1
    while cociente>=1:
        restos[a]=(cociente%2)
        cociente/=2
        a-=1
    lista=""
    for a in range (-1, (-1*len(restos))-1, -1):
        lista+=str(restos[a])
    return "1"+lista+"1"
        
    
    
    
def generalista (longitud):
    lista=[]
    for n in range (binario(longitud)+1):
        lista.append(numeroabinario(n, longitud))
    return lista

def convierteabase(n, string):
    numero=0
    string=string[::-1]
    for a in range (0, len(string)):
            numero+=int(string[a])*(n**(a))
    return numero

def ListaDeBases(string):
    a=2
    Lista=[]
    while a <=10:
        Lista.append(convierteabase(a, string))
        a+=1
    lista1=""
    for item in Lista:
        if EsPrimo(item)==False:
            return False
        else:
            lista1+=str(EsPrimo(item))+" "
    return lista1

def funcion (N, J):
    longitud=N-2    
    c=[]
    for item in generalista(longitud):
        if ListaDeBases (item) !=  False:
            c.append([item, ListaDeBases(item)])
            if len(c)==J:
                return c
lista=funcion (int(lineas[1][0]), int(lineas[1][1]))
print "Case #1:"
for item in lista:
    print item[0]+" "+item[1]

