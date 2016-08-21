entrada = open('A-large.in','r')
salida = open('A-large.out','w')

casos = int(entrada.readline().rstrip('\n'))
print casos

for caso in xrange(casos):

    caracteres = entrada.readline().rstrip('\n')
    lista = [c for c in caracteres]
    numeros = []

    # Esta el 8? EIGHT
    

    while 'G' in lista:
        lista.remove('E')
        lista.remove('I')
        lista.remove('G')
        lista.remove('H')
        lista.remove('T')
        numeros.append('8')

    # Esta el 2 TWO?
    while 'W' in lista:
        lista.remove('T')
        lista.remove('W')
        lista.remove('O')
        numeros.append('2')

    # Esta el 0 ZERO    ?
    while 'Z' in lista:
        lista.remove('Z')
        lista.remove('E')
        lista.remove('R')
        lista.remove('O')
        numeros.append('0')

    # Esta el 6 SIX    ?
    while 'X' in lista:
        lista.remove('S')
        lista.remove('I')
        lista.remove('X')
        numeros.append('6')

    # Esta el 4 FOUR    ?
    while 'U' in lista:
        lista.remove('F')
        lista.remove('O')
        lista.remove('U')
        lista.remove('R')
        numeros.append('4')

    # Esta el 5 FIVE    ?
    while 'F' in lista:
        lista.remove('F')
        lista.remove('I')
        lista.remove('V')
        lista.remove('E')
        numeros.append('5')

    # Esta el 3 THREE    ?
    while 'H' in lista:
        lista.remove('T')
        lista.remove('H')
        lista.remove('R')
        lista.remove('E')
        lista.remove('E')
        numeros.append('3')

    # Esta el 7 SEVEN    ?
    while 'S' in lista:
        lista.remove('S')
        lista.remove('E')
        lista.remove('V')
        lista.remove('E')
        lista.remove('N')
        numeros.append('7')

    # Esta el 1 ONE    ?
    while 'O' in lista:
        lista.remove('O')
        lista.remove('N')
        lista.remove('E')
        numeros.append('1')

    # Esta el 9 ONE    ?
    while 'N' in lista:
        lista.remove('N')
        lista.remove('I')
        lista.remove('N')
        lista.remove('E')
        numeros.append('9')

    print numeros
    numeros.sort()
    result = ""
    for n in numeros:
        result = result +  n

    salida.write("Case #%d: %s\n" % (caso + 1, result))


