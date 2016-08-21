archivo=open("B-large.in")
lineas=[]
for linea in archivo.readlines():
    lineas.append(linea.strip().split(" "))
def inversa(item):
    inversa=""
    for i in range(-1, -1*(len(str(item)))-1, -1):
        inversa+=item[i]
    return inversa

def convertir(item):
    convertir=""
    for i in range (len(str(item))):
        if item[i]=="+":
            convertir+="-"
        elif item[i]=="-":
            convertir+="+"
    return convertir



def funcion (item):
    inversa=item    
    contador=0
    a=0
    while a<len(inversa):
        if inversa[a] == "-":
            inversa=convertir(inversa[a:])
            contador+=1
            a=0
        else:
            a+=1
        
    return contador

for a in range (1, len(lineas)):
    print "Case #%s:"%(a), funcion (inversa(lineas[a][0]))
