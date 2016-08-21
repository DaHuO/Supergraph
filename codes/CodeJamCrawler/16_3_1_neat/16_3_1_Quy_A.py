__author__ = "Quy Doan"

import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file,"r") as reader:
    with open(output_file, "w") as writer:
        '''Do stuffs'''
        num_of_tests = int(reader.readline())
        for test in range(num_of_tests):
            n = int(reader.readline())
            p = map(int,reader.readline().split())
            total = 0
            for pp in p:
                total += pp
            res = ""
            if n == 2:
                for i in range(p[0]):
                    res += " AB"
            else:
                while total > 0:
                    print p
                    if total == 2:
                        alive = []
                        for i in range(n):
                            if p[i] > 0:
                                alive.append(i)
                        res += " " + chr(alive[0]+ord('A')) + chr(alive[1]+ord('A'))
                        total -= 2
                        p[alive[0]] -= 1
                        p[alive[1]] -= 1
                    else:
                        mx = -1
                        for i in range(n):
                            if mx == -1 or p[mx] < p[i]:
                                mx = i
                        res += " " + chr(mx+ord('A'))
                        total -= 1
                        p[mx] -= 1
            print res
            writer.write("Case #"+str(test+1)+":"+res+"\n")

