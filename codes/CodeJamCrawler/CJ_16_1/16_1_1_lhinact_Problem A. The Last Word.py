#-*- coding: utf-8 -*-
def last_word(S):
    rts = ""
    sz = len(S)
    for i in xrange(sz):
        if not rts:
            rts = S[i]
        else:
            if S[i] < rts[0]:
                rts += S[i]
            else:
                rts = S[i] + rts
    return rts

def deal_input(filename):
    output_name = filename.replace(".in", ".out")
    with open(filename, "r") as fin, open(output_name, "w") as fout:
        all = fin.read().split("\n")
        data_num = int(all[0])
        if data_num != len(all) - 2:
            print "wrong input.\n"
            return
        else:
            for i in xrange(1, data_num+1):
                fout.write("Case #%s: %s\n" % (i, last_word(all[i]) ) )


if __name__ == "__main__":
    deal_input("A-large.in")