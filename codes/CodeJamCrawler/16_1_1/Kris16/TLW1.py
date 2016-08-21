# The Last Word.
with open("A-large.in") as in_fp:
    lines = [i.strip("\n") for i in in_fp.readlines()]
TCs = int(lines[0])

with open("output1.ot", "w") as out_fp:
    for i in range(1,TCs+1):
        x = lines[i]
        y = [x[0]]
        for j in range(len(x)-1):
            if x[j+1]>=y[0]:
                y.insert(0,x[j+1])
            else:
                y.append(x[j+1])
        out_fp.writelines("Case #%s: %s\n"%(i,"".join(y)))
