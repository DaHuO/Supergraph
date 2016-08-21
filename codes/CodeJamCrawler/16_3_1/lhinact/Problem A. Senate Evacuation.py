#-*- coding: utf-8 -*-
from collections import defaultdict
def ase(N, nl):
    rts = []
    left = sum(nl)
    tagl = [(nl[i], i) for i in range(N)]
    while left>0:

        t_nl, t_i = max(tagl)
        c = chr(65 + t_i)
        left -= 1
        nl[t_i] -= 1
        tagl[t_i] = (t_nl-1, t_i)

        n_nl, n_i = max(tagl)
        left -= 1
        nl[n_i] -= 1
        tagl[n_i] = (n_nl-1, n_i)

        tr_nl, tr_i = max(tagl)

        if tr_nl*2 > left:
            left += 1
            nl[n_i] += 1
            tagl[n_i] = (n_nl, n_i)
        else:
            c += chr(65 + n_i)
        rts.append(c)
    return " ".join(rts)

def deal_input(filename):
    global cntmap
    output_name = filename.replace(".in", ".out")
    with open(filename, "r") as fin, open(output_name, "w") as fout:
        all = fin.read().split("\n")
        data_num = int(all[0])
        case = 0
        while case < data_num:
            case += 1
            N = int(all[case*2-1])
            nl = map(int, all[case*2].split(" "))
            fout.write("Case #%s: %s\n" % (case, ase(N, nl)))


if __name__ == "__main__":
    deal_input("A-large.in")