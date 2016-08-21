from math import sqrt; from itertools import count, islice

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def base_x(numeros, x, N):
    somas = []
    for numero in numeros:
        soma = 0
        for i in range(N):
            soma += int(numero[-i-1]) * x ** i
        # print(soma)
        somas.append(soma)
    return somas

with open("small.in", "r") as fin, open("output.out", "w") as fout:
    T = int(fin.readline().strip())
    N, J = [int(x) for x in fin.readline().strip().split()]
    size = N - 2
    numeros = []
    numeros_int = []
    for n in range(2 ** size):
        binario = bin(n)[2:].zfill(size)
        binario = list(binario)
        binario.insert(0,"1")
        binario.append("1")
        # print(binario)
        numeros.append(binario)
        binario = (int(("".join(binario))))
        numeros_int.append([binario])
    # print(numeros)
    for num in numeros_int:
        num.append(False)
    # print(numeros_int)
    # print(numeros)
    print("Binarios gerados")
    numero_base_x = []
    for i in range(2, 11):
        n = base_x(numeros, i, N)
        numero_base_x.append(n)
        for j in range(len(n)):
            if not numeros_int[j][1]:
                # print(n[j])
                numeros_int[j][1] = isPrime(n[j])
        # print(numeros_int)


    print(numeros_int)
    print("Primos encontrados")
    fout.write("Case #1:\n")
    j_counter = 0
    for c in range(len(numeros_int)):
        if not numeros_int[c][1]:
            divisores = []
            for i in range(9):
                # print(numero_base_x[i])
                num_atual = numero_base_x[i][c]
                j = 3
                while j <= int(sqrt(num_atual)):
                    # print(num_atual)
                    if num_atual % j == 0 and (i + 2) % j != 0:
                        divisores.append(j)
                        j = num_atual
                    j += 1

            if len(divisores) == 9:
                j_counter += 1
                fout.write("{} ".format(numeros_int[c][0]))
                for k in range(9):
                    fout.write("{} ".format(divisores[k]))
                fout.write("\n")
            # print(numeros_int[c], j_counter)
            # print(divisores)
            if j_counter >= J:
                break



    print("done")
