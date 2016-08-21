import os

import comum


diretorio = os.path.dirname(os.path.abspath(__file__))
entradas = comum.ler_linhas(diretorio, 'input1.txt')

casos = entradas[0]


def dormiu_depois_de(entrada):
    digitos_unicos = list()
    iteracoes = 0

    while len(digitos_unicos) != 10 and iteracoes < 10000000:
        iteracoes += 1
        ovelhas = int(entrada) * iteracoes

        num_list = list(str(ovelhas))
        for item in num_list:
            if int(item) not in digitos_unicos:
                digitos_unicos.append(int(item))

    if iteracoes == 10000000:
        return "INSOMNIA"
    else:
        return str(ovelhas)

for idx, val in enumerate(entradas[1:]):
    print "Case #" + str(idx+1) + ": " + dormiu_depois_de(val)
