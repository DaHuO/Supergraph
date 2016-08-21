__author__ = 'RAIZ'

def agregarNuevos(contenidos, nuevo):
    contenidos_list = list(contenidos)
    nuevos_list = list(nuevo)
    for valor in nuevos_list:
        if valor not in contenidos_list:
            contenidos += valor
            contenidos_list += valor
    return contenidos

def counting(first_number):
    if(first_number==0):
        return "INSOMNIA"
    contenidos = ""
    i = 1
    nuevo = first_number
    while(len(contenidos)<10):
        nuevo = first_number*i
        contenidos = agregarNuevos(contenidos, str(nuevo))
        i += 1
    return nuevo



#MAIN
numCasos = int(input())
for i in range(1, numCasos+1):
    first_number = int(input())

    response = counting(first_number)

    print("Case #"+str(i)+": "+str(response))
quit()
