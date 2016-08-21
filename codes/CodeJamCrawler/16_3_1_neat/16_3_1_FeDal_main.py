#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

def isvalidroom(senators):
    maxparty=max(senators)
    total = sum(senators)
    if maxparty / float(total) <= 0.5:
        return True
    else:
        return False

def solver(senators):

    order = []
    while sum(senators) > 0:
        if not isvalidroom(senators):
            print "wrong"
            print order
            print senators
            raise AssertionError()

        new_senators = senators[:]
        party = np.argmax(new_senators)
        new_senators[party] = new_senators[party]-1

        if isvalidroom(new_senators):
            order.append(party)
        else:   # try one more
            party2 = np.argmax(new_senators)
            new_senators[party2] = new_senators[party2] - 1
            order.append([party, party2])

        senators = new_senators
    return order

if __name__ == "__main__":

    # ngroups = 3
    # senators=np.array([2, 3, 1])
    # order = solver(senators)
    # str = ""
    # for a in order:
    #     if isinstance(a, list):
    #         for b in a:
    #             str = str + chr(b + ord('A'))
    #     else:
    #         str = str + chr(a + ord('A'))
    #         str = str + " "
    # print str
        # print " ",
    # m = [) for x in order]
    # print order
    # print m
    # quit()

    cases = input()
    for caseNr in xrange(cases):
        ngroups = input()
        str_sen = raw_input().split()
        sen = [int(s) for s in str_sen]
        senators = np.array(sen)
        order = solver(senators)
        str = ""
        for a in order:
            if isinstance(a, list):
                for b in a:
                    str = str + chr(b + ord('A'))
            else:
                str = str + chr(a + ord('A'))
            str = str + " "

        print "Case #%d: %s" % (caseNr+1, str)