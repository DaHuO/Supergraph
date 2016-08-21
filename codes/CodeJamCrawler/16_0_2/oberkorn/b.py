#!/usr/bin/python
import sys
import fileinput

def act(pancakes):
    s = list(pancakes)
    if s[0] == '-':
       n = pancakes.find('+')
       if n == -1:
          n = len(pancakes)
       for i in range(0,n):
           s[i] = '+'
    else:
       n = pancakes.find('-')
       for i in range(0,n):
           s[i] = '-'
    return ''.join(s)


def main():
    first_line_read = False
    case_num = 0
    for line in fileinput.input():
        if not first_line_read:
             first_line_read = True
             continue
        case_num += 1
        pancakes = line.strip()
        tries = 0
        while pancakes.find('-') >= 0:
           old_pancakes = pancakes
           pancakes = act(old_pancakes)
           if pancakes != old_pancakes:
              tries += 1
           else:
              print >> sys.stderr, "Error"
              sys.exit(-1)
        print "Case #%d: %d" % (case_num, tries)


if __name__ == "__main__":
     main()
