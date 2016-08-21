import sys

with open(sys.argv[1], 'r') as f:
    next(f)
    round = 0
    for l in f:
        count = 1
        l = l.rstrip()
        num = int(l)

        conjunto = set()
        last = None
        auxnum = None
        while len(conjunto) < 10:
            auxnum = num * count
            if auxnum == 0:
                auxnum = "INSOMNIA"
                break

            for i in str(auxnum):
                if i not in conjunto:
                    conjunto.add(i)

                if len(conjunto) == 10:
                    break

            count = count + 1
        round = round + 1
        print ("Case #%d: %s" % (round, str(auxnum)))
