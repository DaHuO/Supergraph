#!/usr/bin/env python
# -*- coding: utf-8 -*-
# this is gonna use a stack.
# Bounded by number of blank stacks we have
# Proposal:
# find the last "-" on the stack and flip everything up
# to that.
# --+-+--+
# ++-+-+++
# +-+--+++
# ++-+-+++
# +-+--+++ X

# if top of stack is minus, flip stack up to last Minus
# if top of stack is plus, flip stack up to last plus
# --+-+--+
# ++-+-+++
# ---+-+++
# +-++++++
# --++++++
# ++++++++ *

# -
# + 1

# -+
# ++ 1

# +-
# --
# ++ 2

# +++ 0

# --+-
# +-++
# --++
# ++++ *

def find_last(lst, elm):
  gen = (len(lst) - 1 - i for i, v in enumerate(reversed(lst)) if v == elm)
  return next(gen, None)

def solve(s):
    count = 0
    while True:
        s = list(s)
        last_minus = find_last(s,"-")
        # print s
        if last_minus == None:
            return count

        if s[0] == "-":
            for x in range(0,(last_minus+1)/2):
                s[x], s[last_minus-x] = s[last_minus-x], s[x]
            for x in xrange(last_minus+1):
                s[x] = "-" if s[x] == "+" else "+"

        else:
            x=0
            while s[x] == "+":
                s[x] = "-"
                x+=1
        # print s
        count+=1

if __name__ == "__main__":
    testcases = input()

    for caseNr in xrange(1, testcases+1):
        cipher = raw_input()
        print("Case #%i: %s" % (caseNr, solve(cipher)))
