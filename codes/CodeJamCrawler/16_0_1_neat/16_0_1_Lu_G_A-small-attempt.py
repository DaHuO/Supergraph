archivo=open("A-large.in")
lineas=[]
for linea in archivo.readlines():
    lineas.append(int(linea.strip()))

def funcion (n):
    digitos=[]
    b=n
    while True:        
        for item in str(b):
            if item not in digitos:
                digitos.append(item)
        
        if len(digitos)==10:     
            return b
            
            
        b+=n

        
for a in range (1, len(lineas)):
    if lineas[a]==0:
        print "Case #%s:"%(a), "INSOMNIA"
    
    else:
        print "Case #%s:"%(a), funcion (lineas[a])
