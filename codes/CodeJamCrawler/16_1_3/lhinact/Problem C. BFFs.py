#-*- coding: utf-8 -*-

def check_used(used, kmap):
    for i in xrange(len(used)):
        if kmap[used[i]] not in (used[i-1], used[(i+1)%len(used)]):
            return False
    return True

def find_max(used, remain, kmap):
    if not remain:
        if check_used(used, kmap):
            #print used
            return len(used)
        else:
            return 0
    cmax = 0
    if not used:
         for k in list(remain):
           cmax = max(cmax, find_max(used + [k], remain - {k}, kmap))

    elif kmap[used[-1]] not in remain:
        if check_used(used, kmap):
            #print used
            cmax = max(cmax, len(used))

        for k in list(remain):
            cmax = max(cmax, find_max(used + [k], remain - {k}, kmap))

    elif kmap[used[-1]] in remain:
        cmax = max(cmax, find_max(used + [kmap[used[-1]]], remain - {kmap[used[-1]]}, kmap))

    return cmax

def bffs(N, kids):
    cmax = 0
    used = {}
    kmap = {}
    for i in xrange(N):
        kmap[i] = kids[i] - 1
    used = []
    remain = set(range(N))
    return find_max(used, remain, kmap)

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
            N = int(all[cnt])
            cnt += 1
            kids = map(int, all[cnt].split(" "))
            #print case
            fout.write("Case #%s: %s\n" % (case, bffs(N, kids)))


if __name__ == "__main__":
    deal_input("C-small-attempt3.in")