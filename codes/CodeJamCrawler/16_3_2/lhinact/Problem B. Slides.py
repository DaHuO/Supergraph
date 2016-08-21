#-*- coding: utf-8 -*-
from collections import defaultdict
def slides(fout, case, B, M):
    if M > 2**(B-2):
        fout.write("Case #%s: IMPOSSIBLE\n" % (case, ))
        return
    else:
        fout.write("Case #%s: POSSIBLE\n" % (case, ))
        cl = []
        M-=1
        while M > 0:
            cl.append(str(M%2))
            M/=2
        cl.reverse()
        fout.write("0"*(B-len(cl)-1))
        fout.write("".join(cl))
        fout.write("1")
        fout.write("\n")
        for i in range(B-1):
            fout.write("0"*(i+2))
            fout.write("1"*(B-i-2))
            fout.write("\n")
    return

def deal_input(filename):
    global cntmap
    output_name = filename.replace(".in", ".out")
    with open(filename, "r") as fin, open(output_name, "w") as fout:
        all = fin.read().split("\n")
        data_num = int(all[0])
        case = 0
        while case < data_num:
            case += 1
            B, M = map(int, all[case].split(" "))
            slides(fout, case, B, M)
            #fout.write("Case #%s: %s\n" % (case, slides(B, M)))


if __name__ == "__main__":
    deal_input("B-large.in")