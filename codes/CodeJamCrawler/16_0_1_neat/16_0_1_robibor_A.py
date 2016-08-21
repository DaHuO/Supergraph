
def solve(N):
    auxdi = {}
    for el in range(10):
        auxdi[repr(el)] = None
    inserted = 0
    auxdi = {}
    end = False
    if N == 0:
        return "INSOMNIA"
    mult = 1
    help = 0
    while not end:
        newN = mult*N
        N_s = repr(newN)
        nullacambia = False
        for el in N_s:
            if not auxdi.get(el):
                nullacambia = True
                auxdi[el] = newN
                inserted += 1
        mult += 1
        if nullacambia:
            help += 1
        if inserted == 10:
            return newN
        if help > 1000:
            return "INSOMNIA"


def read():
    with open("A-large.in", "r") as filein:
        with open("largeA.txt", "w") as fileout:
            lines = filein.readlines()
            ii=1
            for line in lines[1:]:
                N = int(line.strip())
                out = solve(N)
                mystr = "Case #" + str(ii) + ": " + str(out) + "\n"
                ii += 1
                fileout.write(mystr)


if __name__ == '__main__':
    read()