#! /usr/bin/env python3
#-*- coding: utf8 -*-
import sys

def happy_pancakes(SS, count_string):
    target = "".join(["+" for _ in range(len(SS))])
    ii = 0
    plus_stack = len(SS) - 1
    print(SS, file=sys.stderr)
    while (SS != target):
        jj = plus_stack
        # Find from where the stack must be returned
        while (SS[jj] == "+"):
            jj -= 1
            if (jj < 0):
                print(count_string + str(ii))
                return
        # The first symbol must be a "-" for a return_stack to make sense
        if (jj != 0 and SS[0] != "-"):
            sj = 1
            while (SS[sj] != "-"):
                sj += 1
            SS = return_stack(SS, sj-1)
            ii += 1
        SS = return_stack(SS, jj)
        #print(SS, file=sys.stderr)
        plus_stack = jj
        ii += 1
        while (SS[plus_stack] == "+" and plus_stack > 0):
            plus_stack -= 1
    print(count_string + str(ii))

def return_stack(SS, jj):
    new_SS = ""
    for ii in range(jj+1):
        if (SS[jj-ii] == "+"):
            new_SS += "-"
        else:
            new_SS += "+"
    if (jj < len(SS)):
        new_SS += SS[(jj+1):]
    return(new_SS)


if __name__ == "__main__":
    TT = int(input())
    for ii in range(TT):
        happy_pancakes(input(), "Case #" + str(ii+1) + ": ")

