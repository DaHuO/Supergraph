import fileinput

def main():

    T = 0

    for i, line in enumerate(fileinput.input()):
        if i == 0:
            T = int(line.replace("\n", ""))
            continue
        print("Case #" + str(i) + ": " + str(flipAllPancakes(line.replace("\n", ""))))

def flipAllPancakes(str):

    if str == len(str) * "-":
        return 1

    quant = 0

    while str != len(str) * "+":
        quantP = 0
        quantM = 0
        last = str[0]
        for i in str:
            if i == "+":
                quantP += 1
            else:
                quantM += 1

            if last != i:
                q = quantP if i == "-" else quantM
                str = flipGrup(str, q)
                quant += 1
                break

        if str == len(str) * "-":
            return quant + 1

    return quant

def flipGrup(str, quant):
    aux = str[0:quant]
    #concatena o subvetor trocando as faces
    aux = ''.join(["+" if aux[i] == "-" else "-" for i in range(0, quant)])
    #inverte e soma com o restante
    s = aux[::-1] + str[quant:len(str)]
    return s

if __name__ == "__main__":
    main()