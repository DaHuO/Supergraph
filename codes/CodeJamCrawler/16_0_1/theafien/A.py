#-*- coding: utf-8 -*-


sleep = ['0','1','2','3','4','5','6','7','8','9']

def solve(N):
    if N < 1:
        return "INSOMNIA"

    gabiX = 1

    t = []

    while 1:

        t = t + [x for x in "%s" % (gabiX * N)]
        t = list(set(t))
        t.sort()

        #print t

        if (t == sleep):
            return gabiX * N

        gabiX += 1


def run():
    T = int(raw_input(''))
    i = 1
    while i <= T:
        N = int(raw_input(''))
        print "Case #%d: %s" % (i, solve(N))
        i = i+1


run()