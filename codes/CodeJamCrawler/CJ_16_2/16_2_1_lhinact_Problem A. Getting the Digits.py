#-*- coding: utf-8 -*-
from collections import defaultdict
def gtd(instr):
    rts = []
    inlist = defaultdict(int)
    for x in instr:
        inlist[x] += 1

    if True:
        while inlist["Z"] > 0:
            rts.append(0)
            inlist["Z"] -= 1
            inlist["E"] -= 1
            inlist["R"] -= 1
            inlist["O"] -= 1

        while inlist["W"] > 0:
            rts.append(2)
            inlist["T"] -= 1
            inlist["W"] -= 1
            inlist["O"] -= 1

        while inlist["U"] > 0:
            rts.append(4)
            inlist["F"] -= 1
            inlist["O"] -= 1
            inlist["U"] -= 1
            inlist["R"] -= 1

        while inlist["X"] > 0:
            rts.append(6)
            inlist["S"] -= 1
            inlist["I"] -= 1
            inlist["X"] -= 1

        while inlist["R"] > 0:
            rts.append(3)
            inlist["T"] -= 1
            inlist["H"] -= 1
            inlist["R"] -= 1
            inlist["E"] -= 2

        while inlist["G"] > 0:
            rts.append(8)
            inlist["E"] -= 1
            inlist["I"] -= 1
            inlist["G"] -= 1
            inlist["H"] -= 1
            inlist["T"] -= 1

        while inlist["O"] > 0:
            rts.append(1)
            inlist["O"] -= 1
            inlist["N"] -= 1
            inlist["E"] -= 1

        while inlist["F"] > 0:
            rts.append(5)
            inlist["F"] -= 1
            inlist["I"] -= 1
            inlist["V"] -= 1
            inlist["E"] -= 1

        while inlist["V"] > 0:
            rts.append(7)
            inlist["S"] -= 1
            inlist["E"] -= 2
            inlist["V"] -= 1
            inlist["N"] -= 1

        while inlist["N"] > 0:
            rts.append(9)
            inlist["I"] -= 1
            inlist["N"] -= 2
            inlist["E"] -= 1

    rts.sort()
    return "".join(map(str, rts))

def deal_input(filename):
    global cntmap
    output_name = filename.replace(".in", ".out")
    with open(filename, "r") as fin, open(output_name, "w") as fout:
        all = fin.read().split("\n")
        data_num = int(all[0])
        case = 0
        while case < data_num:
            case += 1
            fout.write("Case #%s: %s\n" % (case, gtd(all[case])))


if __name__ == "__main__":
    deal_input("A-large.in")