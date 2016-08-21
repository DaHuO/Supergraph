#!/usr/bin/env python
import numpy

def is_majority(distr):
    arr = numpy.array(distr)
    majority = numpy.sum(arr)//2 + 1
    for p in arr:
        if p >= majority:
            return True

    return False

with open("test.txt", "r") as f:
    out = open("out.txt", "w")

    number_of_cases = int(f.readline())
    
    for i in range(0, number_of_cases):
        n = int(f.readline())
        distr_t = f.readline().split()
        print(n)
        print(distr_t)
        distr = [int(x) for x in distr_t]
        tot_sol = ""

        if numpy.sum(numpy.array(distr)) % 2 == 1:
            index = numpy.argmax(numpy.array(distr))
            distr[index] -= 1
            tot_sol += " " + str(chr(65+index))

        # print(tot_sol)
        while numpy.sum(numpy.array(distr)) > 0:
            solution = ""
            for idx, p in enumerate(distr):
                b = False
                for j, p2 in enumerate(distr):
                    
                    distr[idx] -= 1
                    distr[j] -= 1
                    if not is_majority(distr):
                        solution = str(chr(65 + idx)) + str(chr(65+j))
                        b = True
                        break
                    else:
                        distr[idx] += 1
                        distr[j] += 1
                if b:
                    break
            if solution != "":
                tot_sol += " " + solution
                # print(tot_sol)
            # else:
            #     print("wtf")
        
        print("Case #{}: {}".format(i+1, tot_sol))
        out.write("Case #{}: {}\n".format(i+1, tot_sol))
        
        
