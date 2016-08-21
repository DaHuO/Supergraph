#!/usr/bin/env python3
import sys

infile = sys.argv[1]
outfile = "sheep.out"
max_i = 100

with open(infile,'rt') as input_file, open(outfile,'wt') as output_file:
    ncases = int(input_file.readline())
    
    for case in range(1,ncases+1):
        n = int(input_file.readline())
        answer = "INSOMNIA"

        if n != 0:
            seen = set()
            all_digits = False
            for i in range(1,max_i):
                mult = str(n*i)
                seen.update(list(mult))
                if len(seen) == 10:
                    all_digits = True
                    answer = mult
                    break
            if not all_digits:
                print("error for input:{}".format(n))
                raise Exception()

        print("Case #{}: {}".format(case,answer), file=output_file)
        
