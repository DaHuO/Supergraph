import itertools
import numpy as np
# from array import array
import math

# ("ZERO"->"Z", , "TWO" -> "W", , "FOUR"->"U", "FIVE"->"V", "SIX"->"X", "SEVEN" -> "S",
# "ONE"->""
# "NINE"->""
#
# "THREE"->""
# "EIGHT"->"T",


__author__ = 'adilmezghouti'

with open("input.txt","r") as f:
    cases = f.readline()
    S = ""
    solution = []
    for i in range(0,int(cases),1):
        S = f.readline().replace("\n","")
        # print S
        while len(S) > 0:
            # print S
            if S.find('Z') >= 0:
                solution.append('0')
                for c in "ZERO":
                    S = S.replace(c,"",1)
            elif S.find("W") >= 0:
                solution.append('2')
                for c in "TWO":
                    S = S.replace(c,"",1)
            elif S.find("U") >= 0:
                solution.append('4')
                for c in "FOUR":
                    S = S.replace(c,"",1)
            elif S.find("X") >= 0:
                solution.append('6')
                for c in "SIX":
                    S = S.replace(c,"",1)
            elif S.find("S") >= 0:
                solution.append('7')
                for c in "SEVEN":
                    S = S.replace(c,"",1)
            elif S.find("V") >= 0:
                solution.append('5')
                for c in "FIVE":
                    S = S.replace(c,"",1)
            elif S.find("G") >= 0 and S.find("H") >= 0:
                solution.append('8')
                for c in "EIGHT":
                    S = S.replace(c,"",1)
            elif S.find("T") >= 0 and S.find("R") >= 0:
                solution.append('3')
                for c in "THREE":
                    S = S.replace(c,"",1)
            elif S.find("N") >= 0 and S.find("O") >= 0:
                solution.append('1')
                for c in "ONE":
                    S = S.replace(c,"",1)
            else:
                # print S
                solution.append('9')
                for c in "NINE":
                    S = S.replace(c,"",1)

        # print ''.join(sorted(solution))
        print "Case #" + str(i + 1) + ": " + ''.join(sorted(solution))
        solution = []

