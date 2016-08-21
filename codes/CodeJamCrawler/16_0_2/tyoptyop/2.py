#!/usr/bin/env python
#
# >

import sys

def get_nb_pancakes(line):
    char = line[0]
    tmp = 0
    if len(line) == 1:
        return 1
    for i in range(0,len(line)):
#        print "nb_pancakes", i, line[i], line
        if line[i] != char:
            break;
    if line[i] == char:
        return i + 1
    return i
    
h = file(sys.argv[1], "r")
flag = True
results = []
for line in h.readlines():
    if flag == True:
        flag = False
        continue ;
    line = line[:-1]
    nb_turn = 0
    while 1:
        nb_pancakes = get_nb_pancakes(line)
#        print nb_turn, line, nb_pancakes
        if nb_pancakes == len(line) and line[0] == "+":
            results.append(nb_turn)
#            print "result", nb_turn
            break ;
        elif nb_pancakes == len(line) and line[0] == "-":
            results.append(nb_turn + 1)
#            print "result", nb_turn + 1
            break ;
        nb_turn += 1
        
        for i in range(0,nb_pancakes):
            if line[i] == "+":
                line2 = list(line)
                line2[i] = "-"
                line = "".join(line2)
            elif line[i] == "-":
                line2 = list(line)
                line2[i] = "+"
                line = "".join(line2)
            

for i in range(0,len(results)):
    print "Case #%d: %s" % (i+1, results[i])
    

