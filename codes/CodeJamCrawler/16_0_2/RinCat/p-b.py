#!/usr/bin/python3 
import sys

def rev_pancakes(case, s):
    i = 0
    while True:
        s_new = []
        if '-' not in s:
            print("Case #" + str(case) + ": " + str(i))
            return
        else:
            if s[0] == '-':
                c = '+'
            else:
                c = '-'
            index = s.find(c)
            s=rev(s, index)
        i = i +1

def rev(s, index=None):
    s_new = []
    if index == None or index == -1:
        for c in s[::-1]:
            if c == '+':
                s_new.append('-')
            else:
                s_new.append('+')
    else:
        s_new_split = s[0:index]
        for c in s_new_split[::-1]:
            if c == '+':
                s_new.append('-')
            else:
                s_new.append('+')
        s_new = s_new + list(s[index:])
    return ''.join(s_new)


if __name__ == "__main__":
    with open(sys.argv[1], "r", encoding="UTF-8") as f:
        f.readline()
        line = 1
        for d in f:
            rev_pancakes(line, d.strip())
            line = line + 1
        




