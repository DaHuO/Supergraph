import glob

EX_NO = "D"
fns = glob.glob("{}-*.in".format(EX_NO))
largest_attempt = -1
ifn = ""
for fn in fns:
    if "large" in fn:
        ifn = fn
        break
    else:
        attempt = int(fn.strip().rstrip(".in")[-1])
        largest_attempt = attempt if attempt > largest_attempt else largest_attempt
if not ifn:
    ifn = "{}-small-attempt{}.in".format(EX_NO, largest_attempt)
fi = open(ifn, encoding="UTF-8")
results = []
T = 0
ls = fi.readlines()
T = int(ls[0])
datas = ls[1:]
#
for data in datas:
    dl = data.split(" ")
    K, C, S = int(dl[0]), int(dl[1]), int(dl[2])
    results.append(" ".join([str(i + 1) for i in range(K)]) if K <= S else "IMPOSSIBLE")


of = open("{}{}".format(ifn.strip().rstrip(".in"), ".out"), 'w', encoding="UTF-8")
i = 1
for result in results:
    of.write("Case #{}: ".format(i))
    of.write(str(result))
    of.write('\n')
    i += 1
