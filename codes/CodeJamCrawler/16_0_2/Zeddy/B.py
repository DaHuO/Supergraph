if __name__ == "__main__":

    fin = open('B-large.in', 'r')
    fout = open('B-large.out', 'w')

    #fin = open('in.txt', 'r')
    #fout = open('out.txt', 'w')

    cases = int(fin.readline())
    print cases

    for t in range(0, cases):
        flips = 0
        case = fin.readline().rstrip()
        caselen = len(case)
        cur_char = case[caselen-1]
        if cur_char == '-':
            flips += 1

        for i in range(0, caselen - 1)[::-1]:
            if case[i] != cur_char:
                flips += 1
            cur_char = case[i]

        print "Case #%d: %d" % (t+1, flips)
        fout.write("Case #" + str(t+1) + ": " + str(flips) + "\n")

    fin.close()
    fout.close()