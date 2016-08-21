def read():
    with open("D-small.in", "r") as filein:
        with open("Dout_small.txt", "w") as fileout:
            lines = filein.readlines()
            ii=1
            for line in lines[1:]:
                lineaux = line.strip().split()
                K = int(lineaux[0])
                C = lineaux[1]
                S = lineaux[2]
                aux=[repr(el) for el in range(1, K+1)]
                out = ' '.join(aux).strip()
                mystr = "Case #" + str(ii) + ": " + out + "\n"
                ii += 1
                fileout.write(mystr)

if __name__ == '__main__':
    read()