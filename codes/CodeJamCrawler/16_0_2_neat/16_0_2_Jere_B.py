from itertools import groupby

def flip(pancakes):
    if pancakes.endswith("+"):
        return (len(pancakes)-1)
    else:
        return (len(pancakes))

if __name__ == "__main__":
    f = open("B-large.in.txt","r")
    o = open("Output.txt","w")
    T = int(f.readline())
    for zz in range(1,T+1):
        case = str(raw_input())
        print case
        case = "".join(a for a, _ in groupby(case))
        output = str.format("Case #%s: %s\n" % (zz, str(flip(case))))
        print output
        o.write(output)
    o.close()
