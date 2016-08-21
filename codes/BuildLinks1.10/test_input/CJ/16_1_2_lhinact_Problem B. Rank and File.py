#-*- coding: utf-8 -*-
def rank_file(N, grids):
    rts = []
    num_cnt = {}
    for i in xrange(2*N-1):
        for j in xrange(N):
            cn = grids[i][j]
            if cn not in num_cnt:
                num_cnt[cn] = 1
            else:
                num_cnt[cn] += 1
    for ks in num_cnt:
        if num_cnt[ks]%2 == 1:
            rts.append(ks)
    rts.sort()
    return rts

def deal_input(filename):
    output_name = filename.replace(".in", ".out")
    with open(filename, "r") as fin, open(output_name, "w") as fout:
        all = fin.read().split("\n")
        data_num = int(all[0])
        cnt = 0
        case = 0
        while case < data_num:
            cnt += 1
            case += 1
            grids = []
            N = int(all[cnt])
            for i in xrange(2*N-1):
                cnt += 1
                grids.append(map(int, all[cnt].split(" ")))
            fout.write("Case #%s: %s\n" % (case, " ".join(map(str, rank_file(N, grids) )) ))


if __name__ == "__main__":
    deal_input("B-large.in")