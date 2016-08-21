import sys

def regroup(pnks):
    current = "~"#pnks[0]
    res = ""
    n_max = len(pnks)-1
    for k,pnk in enumerate(pnks):
        if pnk != current:
            res += pnk
            current = pnk
            # if k == n_max:
            #     res += current
    return res

def calc_n_flips(pnks):
    pnk_regrouped = regroup(pnks)
    tmp = len(filter(lambda x:x == '-',pnk_regrouped))
    if tmp == 0:
        return 0
    return max(k for (k,p) in [(k+1,x == "-") for k,x in enumerate(pnk_regrouped)] if p)

def getData(fileName):
    f = open(fileName, 'r+')
    lines = [line for line in f]
    nCases = int(lines[0])
    k = 1
    while k <= nCases:
        tmp = lines[k]
        result = calc_n_flips(tmp)
        print "Case #"+str(k)+": "+str(result)
        k = k+1

if __name__ == "__main__":
    fileName = sys.argv[1]
    getData(fileName)


