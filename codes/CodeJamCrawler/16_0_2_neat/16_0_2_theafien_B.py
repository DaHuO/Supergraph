#-*- coding: utf-8 -*-

# Gabriella,, te amo <3

def solve(S):

    kV = [x for x in S]

    n = 0
    

    while 1:

        y = "".join(kV).rfind('-')

        if y == -1:
            ##print kV
            return n

        x = 0

        while x <= y:

            if kV[x] == '+':
                kV[x] = '-'
            else:
                kV[x] = '+'

            x += 1 

        n += 1




def run():
    T = int(raw_input(''))
    i = 1
    while i <= T:
        S = str(raw_input(''))
        print "Case #%d: %s" % (i, solve(S))
        i = i+1


run()