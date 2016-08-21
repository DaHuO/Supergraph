#! /usr/bin/env python3

import string

def get_winner(s):
    win = []

    for c in s:
        if win:
            if string.ascii_uppercase.index(c) >= string.ascii_uppercase.index(win[0]):
                win.insert(0, c)
            else:
                win.append(c)
        else:
            win.append(c)

    return "".join(win)

if __name__ == "__main__":
    casecount = int(input())

    for _ in range(casecount):
        print("Case #%d: %s" % ((_ + 1), get_winner(input())))
