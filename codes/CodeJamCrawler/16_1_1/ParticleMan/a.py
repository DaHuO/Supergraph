#!/usr/bin/env python

def printResult(case, result):
    print "Case #{}: {}".format(case, str(result))

if __name__ == "__main__":    
    t = int(raw_input())
    for i in xrange(1, t + 1):
        word, = [str(s) for s in raw_input().split(" ")]
        final = ''
        for letter in word:
            if final == '':
                final = letter
            else:
                if letter >= final[0]:
                    final = letter + final
                else:
                    final = final + letter
        printResult(i, final)
