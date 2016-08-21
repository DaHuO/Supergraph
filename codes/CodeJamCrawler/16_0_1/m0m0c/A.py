
def main():
    fhan = open("small.in")
    out = open("out.txt", "w")
    tc = 1
    firstline = True
    for line in fhan:
        if(firstline == True):
            firstline = False
            continue
        n = int(line)
        base = n
        out.write("Case #" + str(tc) + ": ")
        tc += 1
        if n == 0:
            out.write("INSOMNIA\n")
            continue
        dig = dict()
        cntdig = 0
        while True:
            item = str(n)
            for c in item:
                if c in dig:    continue
                dig[c] = True
                cntdig += 1
            if cntdig == 10: break
            n += base
            if(n < 0):
                print "error"

        out.write(str(n)+'\n')

if __name__ == '__main__':
    main()