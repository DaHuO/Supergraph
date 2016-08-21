archivo=open("A-large.in")
lineas=[]
for linea in archivo.readlines():
    lineas.append(linea.strip().split(" "))


def funcion (palabra):
    palabrafinal=""
    palabrafinal+=palabra[0]
    for a in range (1, len (palabra)):
        
        if palabra[a]<palabrafinal[0]:
            palabrafinal+=palabra[a]
        else:
            palabrafinal=palabra[a]+palabrafinal
    return palabrafinal
for a in range (1, len(lineas)):
     print "Case #%s:"%(a), funcion (lineas[a][0])
