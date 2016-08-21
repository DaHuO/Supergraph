# counting sheep

entrada = open('large.in','r')
salida = open('output-large.out','w')

casos = int(entrada.readline().rstrip('\n'))

for caso in xrange(casos):

    numero_inicial = int(entrada.readline().rstrip('\n'))
    indice = 1

    quedan = map(str,range(10))
    numero = numero_inicial

    if numero_inicial == 0:
        res = "INSOMNIA"
    else:
        res = False


    while not res:
        s_numero = str(numero)

        num_restantes = len(quedan)
        for cifra in s_numero:
            if cifra in quedan:
                quedan.remove(cifra)

        if len(quedan) == 0:
            res = s_numero
        else:
            indice = indice + 1
            numero = numero + numero_inicial

    salida.write("Case #%d: %s\n" % (caso + 1, res))



    

