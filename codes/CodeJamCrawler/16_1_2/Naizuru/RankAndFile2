f = open( 'BLinput.in' , 'r' )
line = f.readline()
contador = 0
case = 1
while line :
    line = line[0:len(line)-1]
    linea = line.split(' ')
    #print linea
    if contador==0:
        cantDeCases = linea[0]
        contador =1
    elif contador==1:
        numero = int(linea[0])
        cantLineaDelCase = (2*numero)-1
        dicc = {}
        for x in range(0, cantLineaDelCase):
            line = f.readline()
            line = line[0:len(line)-1]
            linea = line.split(' ')
            for char in linea:
                #print char
                if char in dicc:
                    dicc[char] +=1 
                else:
                    dicc[char] = 1
        resultado = []
        for char in dicc:
            if not dicc[char] % 2 == 0:
                resultado.append(char) 
        #print resultado
        resultado = [int(numero) for numero in resultado]
        resultado.sort()
        sres = "Case #"+str(case)+": "
        for numero in resultado:
            sres = sres + str(numero) +" "
        print sres
        case +=1
    line = f.readline()
f.close()